#!/usr/bin/env python
#encoding: utf-8

import urllib2

response = urllib2.urlopen('http://python.org/')
f = open("html_doc.txt", "w")
f.write(response.read())
f.close()
