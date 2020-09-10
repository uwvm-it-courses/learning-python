def multiply(a,b):
    print('s= ',a,'*',b, '=', a*b)

def printMax (x, y, z):
 if x>y and x>z :
     print("max x=",x)
 elif y>x and y>z :
     print("max y=",y)
 elif x==y and y==z :
     print("x=y=z")
 elif x==y :
     print("x=y") 
 elif x==z :
     print("x=z")
 elif y==z :
     print("y=z")
 else:
     print("max z=",z)

print("Hello Marina")
  
from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("today =", d1)

print("x= ")
x=int(input())
print("x=",x)

print ("y=")
y=int(input())
print("y=",y)

print ("z=")
z=int(input())
print("z=",z)

printMax (x, y, z)

print("a= ")
a=int(input())
print("a=",a)

print ("b=")
b=int(input())
print("b=",b)

multiply(a,b)
