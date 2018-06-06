import math
import os

# Zadanie 1

napis = input("Podaj napis\n")
lista = [(slowo, len(slowo)) for slowo in napis.split()]
print(lista)

# Zadanie 2

n = input("Podaj liczbe wyrazow ciagu\n")
goldenRatio = (1+5**0.5)/2
fib = [int(( (goldenRatio)**i - (1 - goldenRatio)**i) / (5**0.5) ) for i in range (0,int(n))]
print (fib)

# Zadanie 3

lista = [1,2,3,4,5,6]

def flog(n):
  if n%2 == 0:
    return True
  else:
    return False


def f(flogiczna, lista):
  new_lista = [i for i in lista if flog(i) == True]
  return new_lista
  
print(f(flog,lista))
  
  
# Zadanie 4

def f(lista_p, p_kontorlny):
  new_list =[]
  for i in range (0, len(lista_p)):
    new_list.append((sqrt((lista_p[i][0] - p_kontorlny[0])**2 + (lista_p[i][1] - p_kontorlny[1])**2), ((lista_p[i][0]), (lista_p[i][1]))))
  list_sort = sorted(new_list, key = lambda tup: tup[0])
  return list_sort

lista_punktow = [(1,0), (3,1), (5,9), (8,2), (4,1)]
punkt_kontrolny = (0,0)
print(f(lista_punktow, punkt_kontrolny))

# Zadnanie 5

def generator(p, e):
    for file in os.listdir(p):
        temp = file.split('.')
        if temp[1] == e:
            yield file

path = input("Podaj sciezke \n")
ext = input("Podaj rozszerzenie plikow \n")

for file1 in generator(path, ext):
    print(file1)
