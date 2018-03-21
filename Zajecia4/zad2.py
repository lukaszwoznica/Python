#!/usr/bin/env python
#encoding: utf-8

import sys

slownik = {}

with open(sys.argv[1], "r") as f:
	napis = f.read()


for linia in filter(None, napis.splitlines()):
	wyrazy = linia.split(":")
	slownik[wyrazy[0]] = wyrazy[1]

print slownik
