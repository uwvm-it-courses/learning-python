def matrix():
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
        
matrix ()



