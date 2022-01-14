def bubble_sort1(arr):
    n = len(arr)
    swap = 0
    for i in range(n-1):            # if we use this method it takes (34) swaps to complete sorting
        for j in range(n-i-1):      # its n-i-1 because for every iteration last element will get sorted 
            if arr[j] > arr[j + 1] :        # so we don't need to traverse upto ending of array
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap+=1
    print(*arr,sep=',')
    print('no of swaps performed :' , swap)

l = [44,48,59,39,24,3,20,90,32,64,78,10]
# l = list(map(int,input().split()))
bubble_sort2(l)

# Time Complexity : O(n^2)
# Space Complexity : O(1)