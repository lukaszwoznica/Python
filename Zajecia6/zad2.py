#!/usr/bin/env python
#encoding: utf-8

import re

class WrongMailException(Exception):
    pass

class E_Mail:
	address = ''
	def __init__(self, e_mail):
		if not re.match('[^@]+@[^@]+\.[^@]+', e_mail):
			raise WrongMailException("Podano niepoprawny adres e-mail!")
		else:
			self.address = e_mail

email = E_Mail('lukasz@gmail.com')
print (email.address)
       
