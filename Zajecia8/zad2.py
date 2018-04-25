#!/usr/bin/env python
#encoding: utf-8

import subprocess
import os

subprocess.check_output(["mkdir K1"], shell=True)
subprocess.check_output(["mkdir K1/K2"], shell=True)
subprocess.check_output(["mkdir K1/K3"], shell=True)
subprocess.check_output(["mkdir K1/K3/K4"], shell=True)
subprocess.check_output(["mkdir K5"], shell=True)
subprocess.check_output(["mkdir K5/K6"], shell=True)
