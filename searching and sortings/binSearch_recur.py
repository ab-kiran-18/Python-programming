def binary_search(arr,lo,hi,key):
    if hi >= lo:
        mid = lo + (hi - lo) // 2;
        if arr[mid] == key :
            return True
        elif arr[mid] < key :
            return binary_search(arr, mid + 1, hi, key)
        else:
            return binary_search(arr, lo, mid - 1, key)
    else:  
        return False

l = list(map(int,input('enter array elements :').split()))
key = int(input('enter element to be searched :'))
l.sort()
print(*l,sep=',')
if binary_search(l, key) :
    print('element is found..')
else:
    print('element is not present..')