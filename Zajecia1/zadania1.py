# Zadanie 1

imie = input('Podaj imie\n')
nazwisko = input('Podaj nazwisko\n')
wiek = input('Podaj wiek\n')

print('Czesc ' + imie + ' ' + nazwisko + ', ')
if(int(wiek) < 18):
    print('jestes niepelnoletni')
else:
    print('jestes pelnoletni')
  
# Zadanie 2

l1 = input('Podaj liczbe 1\n')
l2 = input('Podaj liczbe 2\n')
l3 = input('Podaj liczbe 3\n')

if(l1 > l2 and l1 > l3):
    print(str(l1) + '\n')
elif(l2 > l1 and l2 > l3):
    print(str(l2) + '\n')
else:
    print(str(l3) + '\n')
    
# Zadanie 3

i = 97

while(i <= 122):
    print(chr(i) + chr(i-32))
    i += 1
    
# Zadanie 4

i = 97

n = input('Podaj n \n')

while(i <= 122):
    print(chr(i) + chr(i-32))
    i += int(n)
    
# Zadanie 5

n = input('Podaj n \n')
sort_type = input("Sortowanie 0 - rosnaco; 1 - malecjaco\n")

i = 0
lista = []
while(i < int(n)):
    x = input();
    lista.append(int(x));
    i += 1
    
if(sort_type == 0):
    lista.sort()
else:
    lista.sort(reverse = True)
    
zak1 = input('Zakres - liczba1\n')
zak2 = input('Zakres - liczba2\n')    

i = int(zak1)

while (i <= int(zak2)):
    print(lista[i])
    i += 1
    
# Zadanie 6

def fib(n):
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)

n = input("Podaj ilosc wyrazow ciagu\n")
i = 0;
while(i < int(n)):
    print(fib(int(i)))
i += 1
