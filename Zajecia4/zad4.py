#!/usr/bin/env python
#encoding: utf-8

import sys

slownik={}

if(sys.argv[1]!="-"):
	with open(sys.argv[1], "r") as f:
		for line in f:
			if(line.find(sys.argv[2])!=-1):
				print line
else:
	ch = raw_input()
	load = ""
	while(ch != " "):
		load = load + " " + ch
		ch = raw_input()
	print load
