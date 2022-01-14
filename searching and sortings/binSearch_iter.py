def binary_search(arr,key):
    l = 0
    h = len(arr) - 1
    while l <= h:
        mid = l + (h - l) // 2;
        if arr[mid] == key :
            return True
        elif arr[mid] < key :
            l = mid + 1
        else:
            h = mid - 1
    return False

l = list(map(int,input('enter array elements :').split()))
key = int(input('enter element to be searched :'))
l.sort()
print(*l,sep=',')
if binary_search(l, key) :
    print('element is found..')
else: 
    print('element is not present..')

# Time Complexity : O(Log N)
# Space Complexity : O(1)