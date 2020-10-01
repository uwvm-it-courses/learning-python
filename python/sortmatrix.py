def matrixrandom8x10 ():
    from random import random
    N= 8
    M= 10
    a =[]
    for i in range (N):
        z =[]
        for j in range (M):
            n = int(random()*100)
            z.append(n)
            print(n, end = ' ')
        print()
        a.append(z)
    print()
    b=[]
    count=0
    while count < N:
        b += a[count]
        count+=1
    print(b)
    for i in range(len(b)):
        for j in range(len(b)-1):
            if b[j] > b[j + 1]:
                buff = b[j]
                b[j] = b[j + 1]
                b[j + 1] = buff
    print(b)
    g = []
    for i in range (N):
        h =[]
        for j in range (M):
            h.append(b[i*M+j])
        print(h, end = ' ')
        print()
        g.append(h)
    print()

def matrixrandom2x3 ():
    from random import random
    N= 2
    M= 3
    a =[]
    for i in range (N):
        z =[]
        for j in range (M):
            n = int(random()*100)
            z.append(n)
            print(n, end = ' ')
        print()
        a.append(z)
    print()
    b=[]
    count=0
    while count < N:
        b += a[count]
        count+=1
    print(b)
    for i in range(len(b)):
        for j in range(len(b)-1):
            if b[j] > b[j + 1]:
                buff = b[j]
                b[j] = b[j + 1]
                b[j + 1] = buff
    print(b)
    g = []
    for i in range (N):
        h =[]
        for j in range (M):
            h.append(b[i*M+j])
        print(h, end = ' ')
        print()
        g.append(h)
    print()

def matrixrandom(N, M):
    from random import random
    a =[]
    for i in range (N):
        z =[]
        for j in range (M):
            n = int(random()*100)
            z.append(n)
            print(n, end = ' ')
        print()
        a.append(z)
    print()
    b=[]
    for i in range(N):
        for j in range(M):
            b.append(a[i][j])
    print(b)   
    for i in range(len(b)):
        for j in range(len(b)-1):
            if b[j] > b[j + 1]:
                buff = b[j]
                b[j] = b[j + 1]
                b[j + 1] = buff
    print(b)
    g = []
    for i in range (N):
        h =[]
        for j in range (M):
            h.append(b[i*M+j])
        print(h, end = ' ')
        print()
        g.append(h)
    print()
    
matrixrandom8x10 ()
matrixrandom2x3()
matrixrandom(4, 8)
