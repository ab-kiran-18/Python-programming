def length_of_long_AP(set,n):
    if n<=2:
        return n
    dp = [[0 for x in range(n)] for y in range(n)]
    ans = 2
    for i in range(n):
        dp[i][n-1]=2
    for j in range(n-2,0,-1):
        i = j-1
        k = j+1
        while(i>=0 and k<=n-1):
            if (set[i] + set[k] < 2*set[j]):
                k+=1
            elif (set[i] + set[k] > 2*set[j]):
                dp[i][j] = 2
                i -= 1
            else:
                dp[i][j] = dp[j][k] + 1
                ans = max(ans,dp[i][j])
                i -= 1
                k += 1
                while(i>=0):
                    dp[i][j] = 2
                    i -= 1
    return ans

l = list(map(int,input().split()))
print(length_of_long_AP(l, len(l)))