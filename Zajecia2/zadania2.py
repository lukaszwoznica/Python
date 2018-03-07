import math

# Zadanie 1

#napis = input("Podaj napis\n")
#lista = [(slowo, len(slowo)) for slowo in napis.split()]
#print(lista)

# Zadanie 2

#n = input("Podaj dlugosc ciagu\n")
#goldenRatio = (1 + 5**0.5)/2
#fib = [int((goldenRatio)**i - (1 - goldenRatio))]

# Zadanie 4

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
  
  
# Zadanie 5

lista_punktow = [(1,2), (4,2), (3,3)]
punkt = (0,0)

def f(lista_p, p_kont):
  nowa_lista = [(int(math.sqrt((p_kont[0] - lista_p[i][0]) * (p_kont[0] - lista_p[i][0]) + (p_kont[1] - lista_p[i][1]) * (p_kont[1] - lista_p[i][1]))), "Punkt") for i in lista_punktow]
  nowa_lista_sort = sorted(nowa_lista, key = lambda tup: tup[0])
  return nowa_lista_sort
  
print(f(lista_punktow, punkt))
