import os
import tarfile
from contextlib import contextmanager

import requests

FILE_NAME = "gsl-latest.tar.gz"
URL = "http://mirror.inode.at/gnu/gsl/" + FILE_NAME


@contextmanager
def run_in_folder(folder):
    current_folder = os.getcwd()
    if not os.path.exists(folder):
        os.makedirs(folder)
    try:
        os.chdir(folder)
        yield
    finally:
        os.chdir(current_folder)


def download_if_needed(download_folder):

    with run_in_folder(download_folder):
        if not os.path.exists(FILE_NAME):
            print("download source code from", URL)
            with open(FILE_NAME, "wb") as fh:
                fh.write(requests.get(URL).content)


def decompress_if_needed(download_folder):
    with run_in_folder(download_folder):
        with tarfile.open(FILE_NAME, "r") as fh:
            gsl_folder = fh.getnames()[0]
            if not os.path.exists(gsl_folder):
                print("extract", FILE_NAME)
                fh.extractall()
        return os.path.join(download_folder, gsl_folder)


def configure_if_needed(folder, target):
    with run_in_folder(folder):
        if not os.path.exists("Makefile"):
            assert (
                os.system("./configure --prefix={target}".format(target=target)) == 0
            ), "running configure failed"


def run_make_if_needed(folder):
    with run_in_folder(folder):
        if not os.path.exists("./statistics/ttest.o"):
            assert os.system("make") == 0, "running make failed"


def run_make_install_if_needed(gsl_folder, target_folder):
    with run_in_folder(gsl_folder):
        if not all(
            os.path.exists(os.path.join(target_folder, sub_folder))
            for sub_folder in ("lib", "bin", "include")
        ):
            assert os.system("make install") == 0, "running make install failed"


def install_gsl_if_needed(download_folder, target_folder):
    download_if_needed(download_folder)
    gsl_folder = decompress_if_needed(download_folder)
    configure_if_needed(gsl_folder, target_folder)
    run_make_if_needed(gsl_folder)
    run_make_install_if_needed(gsl_folder, target_folder)


if __name__ == "__main__":
    install_gsl_if_needed("/tmp/gsl_download", "/tmp/gsl_installation")
