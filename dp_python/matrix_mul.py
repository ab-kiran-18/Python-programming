import sys
dp = [[-1 for i in range(100)] for x in range(100)]

def matrix_mul(p,i,j):
    if i==j:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    dp[i][j] = sys.maxsize
    for k in range(i,j):
        dp[i][j] = min(dp[i][j], (matrix_mul(p, i, k) + matrix_mul(p, k+1, j) + p[i-1]*p[k]*p[j]) )
    return dp[i][j]

arr = [1,2,3,4]
n = len(arr)
print('minimum no of multiplications:',matrix_mul(arr, 1, n-1))
