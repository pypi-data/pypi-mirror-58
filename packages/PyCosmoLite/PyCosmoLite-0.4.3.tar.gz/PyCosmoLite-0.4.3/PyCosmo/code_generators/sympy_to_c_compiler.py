#! /usr/bin/env python
# encoding: utf-8
from __future__ import absolute_import, division, print_function

import functools
import glob
import hashlib
import importlib
import os
import pickle
import sys
import tempfile
from functools import partial

import sympy as sp

from PyCosmo.BoltzmannSolver.generator.Sp2CVisitor import Sp2CVisitor

from .create_curry_class import (align, create_curry_class,
                                 create_interface_onary)


def concat_generator_results(function):
    """code generator methods here *yield* code blocks.
    This decorator then *returns* the concatendated blocks
    as a single string
    """

    @functools.wraps(function)
    def inner(*a, **kw):
        concat = "\n".join(function(*a, **kw))
        stripped = [line.rstrip() for line in concat.split("\n")]
        return "\n".join(stripped)

    return inner


class Symbol(sp.Symbol):
    def c_args_decl(self):
        return self

    as_function_arg = c_args_decl

    def cython_decl(self):
        return "double " + str(self)


def VectorElement(name, index):
    """this is a hack to sublcass from sp.Expr, implementing __init__ on the
    subclass does not work.
    """

    class _VectorElement(sp.Symbol):
        def c_args_decl(self):
            return self

        def __str__(self):
            return self.name + "[" + str(self.index) + "]"

        def as_function_arg(self):
            return Symbol(self.name + str(self.index))

        def cython_decl(self):
            return "double " + self.name + str(self.index)

        @property
        def free_symbols(self):
            return set((self,))

        def __hash__(self):
            return hash(str(self))

        def __eq__(self, other):
            if type(self) != type(other):
                return False
            return self.name == other.name and self.index == other.index

    result = _VectorElement(name)
    result.index = index
    return result


def Vector(name, size):
    """this is a hack to sublcass from sp.Expr, implementing __init__ on the
    subclass does not work.
    """

    class _Vector(sp.Symbol):
        def __str__(self):
            # brackets = "".join("[{}]".format(n) for n in self.access_path)
            return "{}[{}]".format(self.name, self.size)

        def c_args_decl(self):
            return "*" + self.name

        def __getitem__(self, i):
            if not 0 <= i < self.size:
                raise IndexError()
            return VectorElement(self.name, i)

        def as_function_arg(self):
            return "&{}[0]".format(self.name)

        def cython_decl(self):
            return "double [:] {}".format(self.name)

        @property
        def free_symbols(self):
            elements = (VectorElement(self.name, i) for i in range(self.size))
            return set(elements)

        def __hash__(self):
            return hash(str(self))

        def __eq__(self, other):
            if type(self) != type(other):
                return False

            return self.name == other.name and self.size == other.size

    vector = _Vector(name)
    vector.size = size
    return vector


"""
version history:

    0.0.1 initial version
    0.0.2 enforce static linking of gsl
    0.0.3 fix issues caused by static flag + other fixes for ubuntu
    0.0.4 handle infinite integral limit(s)
    0.0.5 handle vectors
"""

MODULE_NAME = "_wrapper"


class Wrapper(object):

    __version__ = (0, 0, 5)  # for correct caching of generated and compiled code

    def __init__(self, globals_=None):
        if globals_ is None:
            globals_ = Globals([])
        self.globals_ = globals_
        self.names = []
        self.args = []
        self.expressions = []

    def add_function(self, name, args, expression):
        self.names.append(name)
        self.args.append(args)
        self.expressions.append(expression)

    def get_unique_id(self):
        data = (
            self.__version__,
            self.names,
            list(map(str, self.args)),
            list(map(str, self.expressions)),
            self.globals_.get_unique_id(),
        )

        return hashlib.md5(pickle.dumps(data)).hexdigest()

    @concat_generator_results
    def header(self):
        yield align(
            """
        |#include <cmath>
        |#include <cstdio>
        |#include <cstring>
        |#include <unordered_map>
        |#include <string>
        |
        |#include <gsl/gsl_integration.h>
        |#include <gsl/gsl_errno.h>
        |
        |using namespace std;
        |
        |typedef void (*error_callback_t)(string, double, double);
        |
        |enum QuadPackMethod {
        |    QNG,
        |    QAG,
        |    QAGI
        |};
        |
        |extern "C" const char * get_last_error_message();
        |extern "C" const char * get_last_warning_message();
        |extern "C" void clear_last_error_message();
        |extern "C" void clear_last_warning_message();
        |extern "C" void set_eps_rel(string id, double value);
        |extern "C" void set_eps_abs(string id, double value);
        |extern "C" void set_max_intervals(string id, size_t value);
        |extern "C" void set_quadpack_method(string id, QuadPackMethod m);
        |extern "C" void set_error_callback(error_callback_t cb);
        |
        """
        )
        yield self.globals_.header()

        for (name, args, expression) in zip(self.names, self.args, self.expressions):
            yield FunctionWrapper(name, expression, args, self.globals_).header()

    @concat_generator_results
    def code(self, header_file_path):
        yield """#include "{header_file_path}"\n""".format(
            header_file_path=header_file_path
        )
        yield self.globals_.code(header_file_path)

        one_ary_interface_class_code = create_interface_onary()

        yield one_ary_interface_class_code

        yield align(
            """
        |#define BUFFER_SIZE_ERROR_MESSAGE 9999
        |
        |#define APPEND(buffer, buffer_size, what) do {\\
        |    strncat(buffer, what, buffer_size - strlen(buffer));\\
        |    } while(0)
        |
        |static char last_error_message[BUFFER_SIZE_ERROR_MESSAGE] = "";
        |static char last_warning_message[BUFFER_SIZE_ERROR_MESSAGE] = "";
        |
        |void set_error_message(const char * prefix, int code)
        |{
        |    last_error_message[0] = 0;
        |    APPEND(last_error_message, BUFFER_SIZE_ERROR_MESSAGE, prefix);
        |    APPEND(last_error_message, BUFFER_SIZE_ERROR_MESSAGE, ": ");
        |    APPEND(last_error_message, BUFFER_SIZE_ERROR_MESSAGE, gsl_strerror(code));
        |}
        |
        |void set_warning_message(const char * message)
        |{
        |    last_warning_message[0] = 0;
        |    APPEND(last_warning_message, BUFFER_SIZE_ERROR_MESSAGE, message);
        |}
        |
        |static unordered_map<string, double> id_to_eps_rel;
        |static unordered_map<string, double> id_to_eps_abs;
        |static unordered_map<string, size_t> id_to_max_intervals;
        |static unordered_map<string, QuadPackMethod> id_to_quadpack_method;
        |static error_callback_t error_callback = 0;
        |
        |extern "C" {
        |    const char * get_last_error_message() { return last_error_message; }
        |    const char * get_last_warning_message() { return last_warning_message; }
        |    void clear_last_error_message() { last_error_message[0] = 0; }
        |    void clear_last_warning_message() { last_warning_message[0] = 0; }
        |    void set_eps_rel(string id, double value) { id_to_eps_rel[id] = value; }
        |    void set_eps_abs(string id, double value) { id_to_eps_abs[id] = value; }
        |    void set_max_intervals(string id, size_t value) {
        |        id_to_max_intervals[id] = value;
        |    }
        |    void set_quadpack_method(string id, QuadPackMethod m) {
        |         id_to_quadpack_method[id] = m;
        |    }
        |    void set_error_callback(error_callback_t cb) { error_callback = cb; }
        |}
        |
        |inline double gsl_function_eval(double x, void * curried_function)
        |{
        |   OneAryFunction * func = (OneAryFunction *) curried_function;
        |   return (*func)(x);
        |}
        |
        |#define BUFFER_SIZE_SMALL 100
        |
        |#define REPORT_ERROR(fmt, arg, code) do { \\
        |    snprintf(buffer, BUFFER_SIZE_SMALL, fmt, arg); \\
        |    set_error_message(buffer, code); \\
        |   } while(0)
        |
        |#define REPORT_WARNING(fmt, arg) do { \\
        |    snprintf(buffer, BUFFER_SIZE_SMALL, fmt, arg); \\
        |    set_warning_message(buffer); \\
        |   } while(0)
        |
        |double quadpack_integration(OneAryFunction *f, const char *id, double low, double high) {
        |    double result, error, eps_rel, eps_abs;
        |    size_t max_intervals;
        |    QuadPackMethod method;
        |    int err_code;
        |    unordered_map<string, double>::const_iterator found_eps;
        |    unordered_map<string, size_t>::const_iterator found_max_intervals;
        |    unordered_map<string, QuadPackMethod>::const_iterator found_method;
        |    char buffer[BUFFER_SIZE_SMALL];
        |
        |    found_method = id_to_quadpack_method.find(id);
        |    if (found_method != id_to_quadpack_method.end())
        |         method = found_method->second;
        |    else {
        |         REPORT_ERROR("no quadpack method set for id '%s'", id, GSL_EINVAL);
        |         return GSL_EINVAL;
        |    }
        |
        |    if (std::isinf(low) || std::isinf(high)) {
        |        if (method != QAGI) {
        |            REPORT_WARNING("switched to QAGI for infinite limit(s) for id '%s'",
        |                           id);
        |            method = QAGI;
        |        }
        |    }
        |    else if (method == QAGI) {
        |        REPORT_ERROR("you must not use QAGI for finite limit(s) for id '%s'",
        |                     id, GSL_EINVAL);
        |       return GSL_EINVAL;
        |
        |    }
        |
        |    found_eps = id_to_eps_rel.find(id);
        |    if (found_eps != id_to_eps_rel.end())
        |         eps_rel = found_eps->second;
        |    else {
        |         REPORT_ERROR("no eps_rel value set for id '%s'", id, GSL_EINVAL);
        |         return GSL_EINVAL;
        |    }
        |
        |    found_eps = id_to_eps_abs.find(id);
        |    if (found_eps != id_to_eps_abs.end())
        |          eps_abs = found_eps->second;
        |    else {
        |         REPORT_ERROR("no eps_abs value set for id '%s'", id, GSL_EINVAL);
        |         return GSL_EINVAL;
        |    }
        |
        |    gsl_function F;
        |    F.function = gsl_function_eval;
        |    F.params = (void *)f;
        |
        |    gsl_integration_workspace *w;
        |    gsl_set_error_handler_off();
        |
        |    if (method == QAG) {
        |        found_max_intervals = id_to_max_intervals.find(id);
        |        if (found_max_intervals != id_to_max_intervals.end())
        |             max_intervals = found_max_intervals->second;
        |        else {
        |            REPORT_ERROR("no max_intervals value set for id '%s'", id, GSL_EINVAL);
        |            return GSL_EINVAL;
        |        }
        |
        |        w = gsl_integration_workspace_alloc(max_intervals);
        |
        |        err_code = gsl_integration_qag(&F, low, high, eps_abs, eps_rel,
        |                                       max_intervals, GSL_INTEG_GAUSS31, w,
        |                                       &result, &error);
        |
        |        if (err_code)
        |            set_error_message("qag from gsl returned", err_code);
        |        else if (error_callback)
        |            error_callback(id, error, error / result);
        |        gsl_integration_workspace_free(w);
        |
        |    } else if (method == QAGI) {
        |
        |        double sign = 1.0;
        |        double temp;
        |        if (low > high) {
        |            sign = -1.0;
        |            temp = low;
        |            low = high;
        |            high= temp;
        |        }
        |
        |        found_max_intervals = id_to_max_intervals.find(id);
        |        if (found_max_intervals != id_to_max_intervals.end())
        |             max_intervals = found_max_intervals->second;
        |        else {
        |            REPORT_ERROR("no max_intervals value set for id '%s'", id, GSL_EINVAL);
        |            return GSL_EINVAL;
        |        }
        |
        |        w = gsl_integration_workspace_alloc(max_intervals);
        |
        |        if (std::isinf(low) && std::isinf(high)) {
        |            err_code = gsl_integration_qagi(&F, eps_abs, eps_rel, max_intervals,
        |                                            w, &result, &error);
        |            if (err_code)
        |                set_error_message("qagi from gsl returned", err_code);
        |        }
        |        else if (std::isinf(low)) {
        |            err_code = gsl_integration_qagil(&F, high, eps_abs, eps_rel,
        |                                             max_intervals, w, &result, &error);
        |            if (err_code)
        |                set_error_message("qagil from gsl returned", err_code);
        |        }
        |        else {
        |            err_code = gsl_integration_qagiu(&F, low, eps_abs, eps_rel,
        |                                             max_intervals, w, &result, &error);
        |            if (err_code)
        |                set_error_message("qagiu from gsl returned", err_code);
        |        }
        |        result *= sign;
        |
        |        if (!err_code && error_callback)
        |            error_callback(id, error, error / result);
        |
        |        gsl_integration_workspace_free(w);
        |
        |    } else {
        |
        |        size_t neval;
        |        err_code = gsl_integration_qng(&F, low, high, eps_abs, eps_rel,
        |                                       &result, &error, &neval);
        |        if (err_code)
        |            set_error_message("qag from gsl returned", err_code);
        |        else if (error_callback)
        |            error_callback(id, error, error / result);
        |    }
        |
        |    return result;
        |}
        """
        )

        for (name, args, expression) in zip(self.names, self.args, self.expressions):
            yield FunctionWrapper(name, expression, args, self.globals_).code(
                header_file_path
            )

    @concat_generator_results
    def cython(self, header_file_path):
        yield align(
            """|# distutils: language = c++
               |
               |from libcpp.string cimport string
               |cimport numpy as np
               |cimport cython
               |
               |import numpy as np
               |import warnings
               |
               |cdef extern from "{header_file_path}":
               |
               |    enum QuadPackMethod:
               |        QNG
               |        QAG
               |        QAGI
               |
               |cdef extern from "{header_file_path}":
               |    ctypedef void (*error_callback_t)(string, double, double)
               |
               |    char * get_last_error_message()
               |    char * get_last_warning_message()
               |    void clear_last_error_message()
               |    void clear_last_warning_message()
               |    void c_set_eps_rel "set_eps_rel"(string, double)
               |    void c_set_eps_rel "set_eps_rel"(string, double)
               |    void c_set_eps_abs "set_eps_abs"(string, double)
               |    void c_set_max_intervals "set_max_intervals"(string, size_t)
               |    void c_set_quadpack_method "set_quadpack_method"(string, QuadPackMethod)
               |    void c_set_error_callback "set_error_callback"(error_callback_t)
            """.format(
                header_file_path=header_file_path
            )
        )

        yield align(
            """
        |def set_eps_rel(str id, double value):
        |    c_set_eps_rel(id.encode("ascii"), value)
        |
        |def set_eps_abs(str id, double value):
        |    c_set_eps_abs(id.encode("ascii"), value)
        |
        |def set_max_intervals(str id, size_t value):
        |    c_set_max_intervals(id.encode("ascii"), value)
        |
        |def set_quadpack_method(str id, str value):
        |    if value == "QNG":
        |       c_set_quadpack_method(id.encode("ascii"), QuadPackMethod.QNG)
        |    elif value == "QAG":
        |       c_set_quadpack_method(id.encode("ascii"), QuadPackMethod.QAG)
        |    elif value == "QAGI":
        |       c_set_quadpack_method(id.encode("ascii"), QuadPackMethod.QAGI)
        |    else:
        |       raise ValueError("unknown quadpack method {}".format(value))
        |
        |cdef dict call_back_map = {}
        |
        |cdef void c_callback(string id, double abs_err, double rel_err):
        |    cdef str py_id = str(id, "ascii")
        |    global call_back_map
        |    if py_id in call_back_map:
        |        call_back_map[py_id](abs_err, rel_err)
        |
        |def set_error_callback(str id, object cb):
        |    global call_back_map
        |    c_set_error_callback(c_callback)
        |    call_back_map[id] = cb
        """
        )

        yield self.globals_.cython(header_file_path)

        for (name, args, expression) in zip(self.names, self.args, self.expressions):
            yield FunctionWrapper(name, expression, args, self.globals_).cython(
                header_file_path
            )


class Globals(object):
    def __init__(self, variables):
        self.variables = variables

    def get_unique_id(self):
        data = list(map(str, self.variables))
        return hashlib.md5(pickle.dumps(data)).hexdigest()

    @concat_generator_results
    def code(self, header_file_path):
        for variable in self.variables:
            yield "static double {name};".format(name=variable)

        yield ""
        for variable in self.variables:
            yield """extern "C" void set_{name}(double _v){{ {name} = _v; }}""".format(
                name=variable
            )
        yield ""

    @concat_generator_results
    def header(self):
        yield """extern "C" { """
        for variable in self.variables:
            yield "    void set_{name}(double _v); ".format(name=variable)

        yield "}"
        yield ""

    @concat_generator_results
    def cython(self, header_file_path):
        if self.variables:
            yield """cdef extern from "{header_file_path}": """.format(
                header_file_path=header_file_path
            )

            for variable in self.variables:
                yield """    void set_{name}(double value)""".format(name=variable)

            yield ""
        yield "def set_globals(**_g):"

        if self.variables:
            for name in self.variables:
                yield """    if "{name}" in _g: set_{name}(<double>_g["{name}"])""".format(
                    name=name
                )

        else:
            yield "    pass"


def Integral(integrand, integration_variable, low, high, id="default"):
    """this function mimics a class, this is why the name starts with a
    capaital I.

    The reason for this function is that the initializer of sp.Function
    does not work with default arguments.
    """

    if "[" in str(integration_variable):
        raise ValueError("dont use array or array elements as integration variable")

    class Integral(sp.Function("Integral", nargs=5)):
        @property
        def free_symbols(self):
            return self.integrand.free_symbols - {self.integration_variable}

        @property
        def integrand(self):
            return self.args[0]

        @property
        def integration_variable(self):
            return self.args[1]

        @property
        def low(self):
            return self.args[2]

        @property
        def high(self):
            return self.args[3]

        @property
        def id(self):
            return self.args[4]

    return Integral(integrand, integration_variable, low, high, id)


class FunctionWrapper:
    def __init__(self, name, expression, variables, globals_):
        assert set(variables) & set(globals_.variables) == set(())
        self.name = name
        self.expression = expression
        self.variables = variables
        self.globals_ = globals_

        self.args = ", ".join(
            "double {}".format(var.c_args_decl()) for var in self.variables
        )

        self.cython_args = ", ".join(
            "{}".format(var.cython_decl()) for var in self.variables
        )

        self.ufunc_args = ", ".join(
            "np.ndarray[np.double_t, ndim=1, cast=True] {}".format(var)
            for var in self.variables
        )
        self.v = Visitor(self.name, self.globals_)

        # this visit call can create integrand and integral functions
        # which are avail at self.v.extra_functions after self.v.visit
        # finished:
        self.c_expression = self.v.visit(self.expression)

    @concat_generator_results
    def code(self, header_file_path):

        # these were created by Visitor class for creating code for
        # sympy Integrals we create integrand and integral functions
        # first, such that the integrator calls don't refer to undefined
        # functions:
        for extra_wrapper in self.v.extra_functions:
            yield extra_wrapper.code(header_file_path)

        # we insert "_" at beginning of c functions to avoid clash with
        # created python analogues:
        yield align(
            """
        |extern "C" double _{name}({args}) {{
        |    return {c_expression};
        |}}
        """.format(
                name=self.name, args=self.args, c_expression=self.c_expression
            )
        )

    @concat_generator_results
    def header(self):
        # we insert "_" at beginning of c functions to avoid clash with
        # cython functions:
        yield align(
            """
        |extern "C" double _{name}({args});
        """
        ).format(name=self.name, args=self.args)

    @concat_generator_results
    def cython(self, header_file_path):
        # we insert "_" at beginning of c functions to avoid clash with
        # cython functions:
        yield align(
            """
        |cdef extern from "{header_file_path}":
        |    double _{name}({args})
        """.lstrip().format(
                header_file_path=header_file_path, name=self.name, args=self.args
            )
        )

        values = ", ".join(str(v.as_function_arg()) for v in self.variables)
        signature = str(self.expression)
        yield align(
            """
        |def {name}({args}):
        |    cdef double result
        |    cdef const char * _error_message
        |    cdef const char * _warning_message
        |    clear_last_error_message()
        |    clear_last_warning_message()
        |    result = _{name}({values})
        |    _warning_message = get_last_warning_message()
        |    if _warning_message[0] != 0:
        |        warnings.warn(str(_warning_message, encoding="utf-8"))
        |    _error_message = get_last_error_message()
        |    if _error_message[0] != 0:
        |          raise ArithmeticError(str(_error_message, encoding="utf-8") +
        |                " when evaluating {signature}"
        |                )
        |    return result
        """.lstrip().format(
                name=self.name,
                args=self.cython_args,
                values=values,
                signature=signature,
            )
        )

        out_dim = len(self.variables)
        if out_dim == 0:
            yield align(
                """
            |def {name}_ufunc():
            |    pass
            """
            ).format(name=self.name)
            return

        result_view_decl = "double[{}]".format(", ".join(":" * out_dim))
        loop_vars = ["_i{}".format(i) for i in range(out_dim)]
        sizes_decl = "cdef size_t {}".format(
            ", ".join("_n{}".format(i) for i in range(out_dim))
        )
        sizes_init = "\n|    ".join(
            "_n{} = len({})".format(i, self.variables[i]) for i in range(out_dim)
        )

        loop_vars_decl = "cdef size_t {}".format(", ".join(loop_vars))
        temp_args_decl = "cdef double {}".format(
            ", ".join("_v{}".format(i) for i in range(out_dim))
        )

        ll = ""
        for i in range(out_dim):
            indent = "    " * i
            variable = self.variables[i]
            ll += "|    {}for _i{} in range(_n{}):  \n".format(indent, i, i)
            ll += "|    {}    _v{} = {}[_i{}]       \n".format(indent, i, variable, i)

        values = ", ".join("_v{}".format(i) for i in range(out_dim))
        index = ", ".join("_i{}".format(i) for i in range(out_dim))
        shape_args = ", ".join("_n{}".format(i) for i in range(out_dim))

        return

        yield align(
            """
        |@cython.boundscheck(False)
        |@cython.wraparound(False)
        |def {name}_ufunc({ufunc_args}):
        |    cdef np.ndarray[np.double_t, ndim={out_dim}, cast=True] result
        |    cdef const char * _error_message
        |    cdef const char * _warning_message
        |    {loop_vars_decl}
        |    {temp_args_decl}
        |    {sizes_decl}
        |    {sizes_init}
        |    result = np.empty(({shape_args}), dtype=np.double)
        |    cdef {result_view_decl} result_view = result
        |    clear_last_warning_message()
        |    clear_last_error_message()
        |
        {nested_loop}
        |    {indent}    result_view[{index}] = _{name}({values})
        |
        |    _warning_message = get_last_warning_message()
        |    if _warning_message[0] != 0:
        |        warnings.warn(str(_warning_message, encoding="utf-8"))
        |
        |    _error_message = get_last_error_message()
        |    if _error_message[0] != 0:
        |          raise ArithmeticError(str(_error_message, encoding="utf-8") +
        |                " when evaluating {signature}"
        |                )
        |    return result
        """.lstrip().format(
                name=self.name,
                ufunc_args=self.ufunc_args,
                out_dim=out_dim,
                result_view_decl=result_view_decl,
                loop_vars_decl=loop_vars_decl,
                temp_args_decl=temp_args_decl,
                sizes_decl=sizes_decl,
                sizes_init=sizes_init,
                shape_args=shape_args,
                signature=signature,
                nested_loop=ll.rstrip(),
                indent=indent,
                index=index,
                values=values,
            )
        )


class Visitor(Sp2CVisitor):
    """this extends the existing Sp2CVisitor to handle Integrals.
    """

    def __init__(self, name, globals_=None):
        Sp2CVisitor.__init__(self)
        self.extra_functions = []
        self.name = name
        if globals_ is None:
            globals_ = Globals([])
        self.globals_ = globals_
        self.integral_count = 0

    def visit_sin(self, expr):
        return "sin({})".format(self.visit(expr.args[0]))

    def visit_cos(self, expr):
        return "cos({})".format(self.visit(expr.args[0]))

    def visit_log(self, expr):
        return "log({})".format(self.visit(expr.args[0]))

    def visit_exp(self, expr):
        return "exp({})".format(self.visit(expr.args[0]))

    def visit_Pi(self, expr):
        return "3.14159265358979323846"

    def visit_Infinity(self, expr):
        return "INFINITY"

    def visit_NegativeInfinity(self, expr):
        return "-INFINITY"

    def visit_Pow(self, expr):
        try:
            return Sp2CVisitor.visit_Pow(self, expr)
        except Exception:
            return "pow({}, {})".format(self.visit(expr.base), self.visit(expr.exp))

    def visit___Vector(self, expr):
        return str(expr)

    def visit__VectorElement(self, expr):
        return str(expr)

    def visit_Integral(self, integral):

        integrand = integral.integrand
        integration_variable = integral.integration_variable
        low = integral.low
        high = integral.high

        # the variables for the integrand. we include the limits here
        # for nested integrals:

        free_variables_integrand = list(
            (integrand.free_symbols | low.free_symbols | high.free_symbols)
            - {integration_variable}
            - set(self.globals_.variables)
        )
        variables_integrand = free_variables_integrand + [integration_variable]

        integrand_name = "_integrand_{}_{}".format(self.name, self.integral_count)
        integral_function_name = "_integral_{}_{}".format(
            self.name, self.integral_count
        )
        self.integral_count += 1

        subs = dict(
            zip(
                free_variables_integrand,
                [v.as_function_arg() for v in free_variables_integrand],
            )
        )

        integrand = integrand.subs(subs)
        low = low.subs(subs)
        high = high.subs(subs)

        self.extra_functions.append(
            FunctionWrapper(
                integrand_name,
                integrand,
                [v.as_function_arg() for v in variables_integrand],
                self.globals_,
            )
        )

        low_expression_in_c = self.visit(low)
        high_expression_in_c = self.visit(high)

        integral_function_wrapper = IntegralFunctionWrapper(
            integral_function_name,
            [v.as_function_arg() for v in free_variables_integrand],
            low_expression_in_c,
            high_expression_in_c,
            integrand_name,
            integral.id,
        )

        self.extra_functions.append(integral_function_wrapper)

        return "{}({})".format(
            integral_function_name,
            ", ".join(str(var) for var in free_variables_integrand)
        )


class IntegralFunctionWrapper(object):
    seen = set()

    @classmethod
    def reset(clz):
        clz.seen = set()

    def __init__(self, name, free_vars, low, high, integrand_name, id):
        self.name = name
        self.free_vars = free_vars
        self.low = low
        self.high = high
        self.integrand_name = integrand_name
        self.id = id

    @concat_generator_results
    def code(self, header_file_path):

        curry_class_name, curry_class_code = create_curry_class(len(self.free_vars))

        # don't craeate same currying abstract base class multiple
        # times:
        if curry_class_name not in self.seen:
            self.seen.add(curry_class_name)
            yield curry_class_code

        args = ", ".join("double {}".format(var) for var in self.free_vars)

        # we insert "_" at beginning of c functions to avoid clash with
        # cython functions:
        cons_args = ", ".join(
            ["_" + self.integrand_name] + list(map(str, self.free_vars))
        )

        yield align(
            """
        |inline double {name}({args}) {{
        |    {curry_class_name} curried_function({cons_args});
        |    return quadpack_integration(&curried_function, "{id}", {low}, {high});
        |}}
        |"""
        ).format(
            name=self.name,
            id=self.id,
            low=self.low,
            high=self.high,
            args=args,
            curry_class_name=curry_class_name,
            cons_args=cons_args,
        )


def generate_files(folder, wrapper, gsl_root):

    if not os.path.exists(folder):
        os.makedirs(folder)

    IntegralFunctionWrapper.reset()

    j = partial(os.path.join, folder)

    with open(j("functions.cpp"), "w") as fh:
        print(wrapper.code("functions.hpp"), file=fh)

    with open(j("functions.hpp"), "w") as fh:
        print(wrapper.header(), file=fh)

    with open(j("{module_name}.pyx".format(module_name=MODULE_NAME)), "w") as fh:
        print(wrapper.cython("functions.hpp"), file=fh)

    setup_py_content = align(
        """#! /usr/bin/env python
    |# encoding: utf-8
    |from __future__ import absolute_import, division, print_function

    |from distutils.core import setup
    |from distutils.extension import Extension
    |
    |from Cython.Build import cythonize
    |import numpy as np
    |
    |sourcefiles = ['{module_name}.pyx', 'functions.cpp']
    |
    |extensions = [Extension("{module_name}",
    |                        sourcefiles,
    |                        define_macros = [('HAVE_INLINE', '1')],
    |                        include_dirs=['{gsl_root}/include', np.get_include()],
    |                        library_dirs=['{gsl_root}/lib'],
    |                        extra_compile_args = ["-std=c++11", "-fPIC"],
    |                        extra_link_args = ["-fPIC"],
    |                        extra_objects = ['{gsl_root}/lib/libgsl.a']
    |                        )
    |              ]
    |
    |setup(
    |   ext_modules=cythonize(extensions)
    |)
    """
    ).format(module_name=MODULE_NAME, gsl_root=gsl_root)

    with open(j("setup.py"), "w") as fh:
        print(setup_py_content, file=fh)


def compile_files(folder):
    try:
        load_wrapper(folder)
        return
    except ImportError:
        pass
    current_folder = os.getcwd()
    try:
        os.chdir(folder)
        os.system("python setup.py build_ext --inplace")
    finally:
        os.chdir(current_folder)


def load_wrapper(folder):

    sys.path.insert(0, folder)
    if MODULE_NAME in sys.modules:
        del sys.modules[MODULE_NAME]
    try:
        wrapper = importlib.import_module(MODULE_NAME)
        return wrapper
    finally:
        sys.path.pop(0)


def compile_if_needed_and_load(wrapper, root_folder=None, gsl_root=None):
    assert gsl_root is not None, "this case is not implemented yet"
    if root_folder is None:
        root_folder = tempfile.mkdtemp()
    build_folder = os.path.join(root_folder, wrapper.get_unique_id())
    if not glob.glob(os.path.join(build_folder, "wrapper*.so")):
        generate_files(build_folder, wrapper, gsl_root)
        compile_files(build_folder)
    return load_wrapper(build_folder)


if __name__ == "__main__":
    v = Visitor("a")
    a = Vector("a")
    expr = a[0] + a[1]
