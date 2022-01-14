def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        MERGE(arr,L,mid,R)

def MERGE(arr,L,mid,R):
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print() 

l = [44,48,59,39,24,3,20,90,32,64,78,10]
mergeSort(l)
printList(l)

# Time Complexity = O(N * Log)