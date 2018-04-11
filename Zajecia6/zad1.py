#!/usr/bin/env python
#encoding: utf-8

def pow(x):
	try:
		result = x ** 0.5
	except (ValueError):
		print('Liczba nie moze byc ujemna!')
	except (TypeError):
		print('Niepoprawny typ w argumencie!')
	else:
		return result


print(pow(4))
