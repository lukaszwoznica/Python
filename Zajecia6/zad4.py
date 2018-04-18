#!/usr/bin/env python
#encoding: utf-8

import urllib2
from xml.dom import minidom

response = urllib2.urlopen('https://www.yr.no/sted/Polen/Lublin/Lublin/forecast.xml')
document = minidom.parse(response)
elements = document.getElementsByTagName("sun")

for e in elements:
	rise = e.getAttribute("rise")

print rise
