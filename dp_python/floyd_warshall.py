def func(g):
    l=[]
    for i in range(len(g)):
        x=[]
        for j in range(len(g[0])):
            x.append(g[i][j])
        l.append(x)
    for k in range(len(g)):
        for i in range(len(g)):
            for j in range(len(g)):
                l[i][j] = min(l[i][j] , l[i][k] + l[k][j])
    print(*l)

g = [[3, 5, 65, 35, 6], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8], [0, 3, 6, 9, 12], [0, 4, 8, 12, 16]]
func(g)