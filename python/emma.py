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
     
def loop1():
    for x in range (1, 11):
        print(x, "Привіт")
        
def loop2():
    i = 1
    while i < 16 :
        print(i, "Привіт")
        i += 1
        
def sayHW () :
    a = "    Привіт Світ   "
    a = (a.strip())
    b = "     Привіт СВІТЛО   "
    b = (b.strip())
    print(a[0 : 5].upper() + a[5 : 11])
    print(b[0 : 8] + b[-5 : ].lower())
    print(a[1] +" " + b[1])
    

    

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

loop1()

loop2()

sayHW ()
