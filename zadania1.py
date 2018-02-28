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
    print(l1 + '\n')
elif(l2 > l1 and l2 > l3):
    print(l2 + '\n')
else:
    print(l3 + '\n')
    
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
sort_type = input("Sortowanie rosnaco/malecjaco\n")

i = 0
lista = []
while(i < int(n)):
    x = input();
    lista.append(int(x));
    i += 1
    
if(sort_type == 'rosnaco'):
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

n = input("Podaj ilosc wyrazow ciagu\n")
liczby = [0,1] 
x = 0
for i in range(int(n)):                  
    x = liczby[-1] + liczby[-2]  
    numbers.append(x)             
    print (x) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    