# Zadanie 1

class LiczbaZespolona(object):
  def __init__(self, re, im):
    self.re = re
    self.im = im
  
  def setRe(self, re):
    self.re = re   
    
  def setIm(self, im):
    self.im = im
    
  def __add__(self, second):
    re = self.re + second.re
    im = self.im + second.im
    return str(re) + " + " + str(im) + "i"
    
  def __sub__(self, second):
    re = self.re - second.re
    im = self.im - second.im
    return str(re) + " + " + str(im) + "i"
    
  def __mul__(self, second):
    re = self.re * second.re - self.im * second.im  
    im = self.re * second.im + self.im * second.re
    return str(re) + " + " + str(im) + "i"
  
  def __truediv__(self, second):
    mod_2 = second.re * second.re + second.im * second.im
    re = (self.re * second.re + self.im * second.im) / mod_2
    im = (second.re * self.im - self.re * second.im) / mod_2;
    return str(re) + " + " + str(im) + "i"
   
  def __eq__(self, second):
    if(self.re == second.re and self.im == second.im):
      return True;
    else:
      return False; 
    
  def mod(self):
    mod = (self.re**2 + self.im**2)**0.5
    if(mod < 0):
      mod = mod * (-1)
    return mod
      


a = LiczbaZespolona(1,2)
b = LiczbaZespolona(1,2)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a.mod())
print(b.mod())
print(a==b)


#Zadanie 2


class Punkt2D(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def odleglosc(self, second):
    dist = ((second.x - self.x)**2 + (second.y - self.y)**2)**0.5
    return dist
      
class Punkt3D(Punkt2D):
  def __init__(self, x, y, z):
    super().__init__(x, y)
    self.z = z
    
  def odleglosc(self, second):
    dist = ((second.x-self.x)**2 + (second.y-self.y)**2 + (second.z-self.z)**2)**0.5
    return dist
    
p2d_1 = Punkt2D(0, 0)
p2d_2 = Punkt2D(3, 3)
p3d_1 = Punkt3D(0, 0, 0)
p3d_2 = Punkt3D(3, 3, 3)
print(p2d_1.odleglosc(p2d_2))
print(p3d_1.odleglosc(p3d_2))
 
# Zadanie 3

class Kolo(object):
  __rozmiar = None
  __markaOpony = None
  
  def __init__(self, rozmiar, markaOpony):
    self.__rozmiar = rozmiar
    self.__markaOpony = markaOpony

  def setRozmiar(self, rozmiar):
    self.__rozmiar = rozmiar
  
  def setMarkaOpony(self, markaOpony):
    self.__markaOpony = markaOpony
  
  def getRozmiar(self):
    return self.__rozmiar
  
  def getMarkaOpony(self):
    return self.__markaOpony
    
  def __str__(self):
    ret = "Kolo: \nRozmiar: "+str(self.__rozmiar)+"\nMarka opony: "+str(self.__markaOpony)
    return ret
    
class Silnik(object):
  __pojemnosc = None
  __moc = None
  
  def __init__(self, pojemnosc, moc):
    self.__pojemnosc = pojemnosc
    self.__moc = moc 
  
  def setPojemnosc(self, pojemnosc):
    self.__pojemnosc = pojemnosc
  
  def setMoc(self, moc):
    self.__moc = moc
  
  def getPojemnosc(self):
    return self.__pojemnosc
  
  def getMoc(self):
    return self.__moc
    
  def __str__(self):
    ret = "Silnik: \nPojemnosc: "+str(self.__pojemnosc)+"\nMoc: "+str(self.__moc)
    return ret
          
class ZbiornikPaliwa(object):
  __maxPojemnosc = None
  __obecnaIlosc = None
    
  def __init__(self, maxPojemnosc):
    self.__maxPojemnosc = maxPojemnosc
   
  def setObecnaIlosc(self, obecnaIlosc):
    self.__obecnaIlosc = obecnaIlosc     

  def getObecnaIlosc(self):
    return self.__obecnaIlosc
    
  def __str__(self):
    ret = "Zbiornik: \nMax ilosc paliwa: "+str(self.__maxPojemnosc)+"\nObecna ilosc paliwa: "+str(self.__obecnaIlosc)
    return ret
    
class Samochod(Kolo, Silnik, ZbiornikPaliwa):
  __marka = None
  __model = None
    
  def __init__(self, marka, model, rozmiarKola, markaOpony, pojemnosc, moc, pojemnoscZbiornika):
    Kolo.__init__(self, rozmiarKola, markaOpony)
    Silnik.__init__(self, pojemnosc, moc)
    ZbiornikPaliwa.__init__(self, pojemnoscZbiornika)
    self.__marka = marka
    self.__model = model
    
  def setMarka(self, marka):
    self.__marka = marka
  
  def setModel(self, model):
    self.__model = model
  
  def getMarka(self):
    return self.__marka
  
  def getModel(self):
    return self.__model
    
  def __str__(self):
    ret = "Samochod:\nMarka: "+str(self.__marka)+"\nModel: "+str(self.__model)
    return ret+"\n" + Silnik.__str__(self) + "\n" + ZbiornikPaliwa.__str__(self) + "\n" + Kolo.__str__(self) + "\n"

sam = Samochod("Audi", "A8", 18, "Michelin", 3.0 , 250, 55)
sam.setObecnaIlosc(40)
print(sam)
