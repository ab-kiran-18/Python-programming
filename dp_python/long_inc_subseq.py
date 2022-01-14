def lis(l,n):
    dp = [1 for i in range(len(l))]
    maxi = l[0]
    for i in range(len(l)):
        dp[i] = 1
        for j in range(i):
            if l[j] <= l[i]:
                dp[i] = max(dp[i],dp[j] + 1)
    return max(dp)
