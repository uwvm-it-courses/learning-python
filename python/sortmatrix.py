
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
    len_b = len(b)
    for i in range(len_b):
        for j in range(len_b-1):
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
    import numpy
    sorted = numpy.array(b)
    print("Sort is correct:", numpy.array_equal(sorted,b))
    
matrixrandom(4, 8)
