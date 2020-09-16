def matrix1():
    N = 5
    a = []
    for i in range (N):
        tmp = []
        for j in range (N):
            if i == j or i == i and j == N-i-1:
                tmp.append(1)
            else:
                tmp.append(0)
        a.append(tmp)
    for row in a:
        print(' '.join([str(elem) for elem in row]))


def matrix2():
    N = 5
    a = [[0] * N for i in range (N)]
    for i in range (N):
        a[i][i] = 1
        a[i][N-i-1] = 1
    for row in a:
        print(' '.join([str(elem) for elem in row]))
    
matrix1 ()
print("------------")
matrix2 ()


