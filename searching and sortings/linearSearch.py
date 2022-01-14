def linear_search(l,key):
    for i in l:
        if i == key:
            return True
    return False

l = list(map(int,input('enter array elements :').split()))
key = int(input('enter element to be searched :'))
if linear_search(l, key) :
    print('element is found..')
else:
    print('element is not present..')