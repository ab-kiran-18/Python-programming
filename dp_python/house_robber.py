def house_robber(l):
    size = len(l)
    if size == 0:
        return 0
    elif size == 1:
        return l[0]
    else:
        dp = [0 for i in range(len(l)+1)]
        dp[0] = l[0]
        dp[1] = max(l[0],l[1])
        for i in range(2,size):
            dp[i] = max(l[i] + dp[i-2] , dp[i-1])
        return dp[-1]

l = list(map(int,input().split()))
print(house_robber(l))