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
