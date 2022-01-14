def build_bridge(north,south,n):
    zip_pairs = zip(south,north)
    z = [x for _,x in sorted(zip_pairs)]
    dp = [1 for i in range(n)]
    for i in range(1,n):
        for j in range(0,i):
            if (north[i] >= north[j] and dp[i] < dp[j] + 1) :
                dp[i] = dp[j] + 1
    maxi = max(dp)
    return maxi
n = list(map(int,input('enter cites in north:').split()))
s = list(map(int,input('enter cites in south:').split()))
print(build_bridge(n, s, len(n)))