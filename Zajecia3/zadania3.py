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
    
p2d_1 = Punkt2D(0,0)
p2d_2 = Punkt2D(2,2)
p3d_1 = Punkt3D(0,0,0)
p3d_2 = Punkt3D(2,2,2)
print(p2d_1.odleglosc(p2d_2))
print(p3d_1.odleglosc(p3d_2))
 
