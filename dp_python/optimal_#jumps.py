def minJump(num, n):
    dp = [n] * (99999999)
    dp[0] = 0
    for i in range(n):
        for j in range(i+1,  min(i+num[i]+1, n)):
            dp[j] = min(dp[j], 1 + dp[i])
    return dp[n-1]

l = list(map(int,input().split()))
print(minJump(l, len(l)))