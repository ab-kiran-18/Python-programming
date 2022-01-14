def func(W,wt,prf,n):
    k = [[0 for i in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0 :
                k[i][w]=0;
            elif wt[i-1] < w:
                k[i][w] = max(prf[i-1] + k[i-1][w-wt[i-1]],k[i-1][w])
            else:
                k[i][w] = k[i-1][w]
    print(*k)

W=6     #bag size
wht = [1 , 2 , 4 ]        #weight array
val = [10,12 , 28]      #profit array
n=3     #no of objects
func(W,wt,val,n)