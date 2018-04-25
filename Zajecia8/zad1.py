#!/usr/bin/env python
#encoding: utf-8

import subprocess
import os

try:
    out = subprocess.check_output(["g++ -o prog prog.cpp"], shell=True)
except subprocess.CalledProcessError as ex:
    print("Błąd kompilacji!")
