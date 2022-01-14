def func(mat,n,m):
    # intializing dp matrix elements all as 0
    dp = [[0 for i in range(m)] for x in range(n)]
    # iterating for calculating
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:       # x an y are null
                dp[i][j] = mat[i][j]
            elif i==0:              # here inserting y values into x
                dp[i][j] = mat[i][j] + dp[i][j-1]
            elif j==0:              # here deleting values from x
                dp[i][j] = mat[i][j] + dp[i-1][j]
            else:                   # here we are replacing x and y
                dp[i][j] = mat[i][j] + max(dp[i-1][j],dp[i][j-1])
    print(dp[n-1][m-1])

mat = [[10,9,4,14],
        [3,8,12,8],
        [3,7,9,8],
        [12,14,19,3]]
n = m = 4
func(mat,n,m)