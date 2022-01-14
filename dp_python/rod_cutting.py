# rod cutting is a variation for unbounded knapsack
def function(length,price,N):
    # intializing dp matrix all elements as 0
    dp = [[0 for i in range(N+1)]for j in range(len(length)+1)]
    # running 2 loops for finding values of dp matrix
    for i in range(N+1):
        for j in range(len(length)+1):
            if i==0 or j==0:            # if length is 0 or price is 0
                dp[i][j] = 0
            elif length[i-1] < N:       #if including
                dp[i][j] = max(dp[i-1][j] , dp[i-1][j-length[i-1]] + price[i-1])
            else:                       # if excluding
                dp[i][j] = dp[i-1][j]   
    print(dp[N-1][N-1])                 # finding maximum profit made

n = int(input())
length_arr = list(map(int,input().split()))
prices_arr = list(map(int,input().split()))
function(length_arr, prices_arr, n)
