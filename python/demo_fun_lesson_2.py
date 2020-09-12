def add(a, b):
    c = a + b
    c += b #c = c + 4
    print('add', int(c))

def mult(a,b,c):
    print('mult',int(a*b*c))
    
def demo():
    add(99,99)
    mult(7,7,8)
    
add(1, 3)
demo()

def add1( a, b, c):
    d = a + b + c
    print('add a,b,c', d)

add1(4, 3, 6)

