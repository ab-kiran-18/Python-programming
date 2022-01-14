def nCr(n,r):
    l = []
    for i in range(n+1):
        l.append([0 for i in range(r+1)])
    for i in range(n+1):
        for j in range(r+1):
            if i==j or j==0:
                l[i][j] = 1
            else:
                l[i][j] = l[i-1][j-1] + l[i-1][j]
    return l[n][r]
n,r = map(int,input('enter n and r values:').split())
print(nCr(n,r))
