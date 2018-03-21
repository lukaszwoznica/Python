#!/usr/bin/env python
#encoding: utf-8

import sys

slownik={}

with open(sys.argv[1], "r") as f:
	for line in f:
		for element in line.split():
			if(element in slownik):
				slownik[element] = slownik[element] + 1
			else:
				slownik[element] = 1

print slownik

