# encoding: utf-8
from __future__ import print_function, division, absolute_import


from PyCosmo._structs import Struct
from sympy import Symbol, Rational

_syms = """a H_0 k Phi delta delta_b u u_b
           taudot_interp c_s_interp eta_interp
           omega_r omega_m omega_k omega_l omega_b omega_gamma omega_neu
           omega_dm """.split()


class SymbolArray:

    def __init__(self, base_symbol):
        self.base_symbol = base_symbol

    def __getitem__(self, idx):
        from sympy import Symbol  # hack to make notebook work
        return Symbol("{}_{}".format(self.base_symbol, idx))


symbols = Struct({
                  "R": Rational,
                  "Theta": SymbolArray("Theta"),
                  "Theta_P": SymbolArray("Theta_P"),
                  "N": SymbolArray("N"),
                 }
                 )

for _name in _syms:
    _name = _name.strip()
    symbols[_name] = Symbol(_name)


try:
    del _syms
    del _name
    del Symbol
    del Rational
    del Struct
except Exception as e:
    print(e)
