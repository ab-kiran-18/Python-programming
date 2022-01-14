def insertion_sort(l):
    n = len(l)
    for i in range(1,n):
        sub_part_elem = l[i]        # it is the ending element of the subarray that
        j = i-1                     # - we are sorting
        while j>=0 and sub_part_elem < l[j] :       # checking whether any element in the subarray is 
            l[j+1] = l[j]                           # - smaller than the last element
            j -= 1
        l[j+1] = sub_part_elem
    print(*l,sep=',')

l = [44,48,59,39,24,3,20,90,32,64,78,10]
insertion_sort(l)

# Time Complexity : O(N^2)
# for Best Case : O(N)
# Space Complexity : O(1)

# Advantages :
# It performs very well on small lists
# It is an in-place algorithm. It does not require a lot of space for sorting. 
#  - Only one extra space is required for holding the temporal variable.

# Disadvantages :
# Insertion sort is inefficient against more extensive data sets
# The insertion sort exhibits the worst-case time complexity of O(n2)
# It does not perform well than other, more advanced sorting algorithms