def selection_Sort(l):
    n = len(l)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if l[j] < l[min_index] :
                min_index = j
        if min_index != 1 :
            l[i], l[min_index] = l[min_index], l[i]
    print(*l,sep=',')     

l = [44,48,59,39,24,3,20,90,32,64,78,10]
selection_Sort(l)

# Time Complexity for (Best,Average,Worst) : O(N^2)
# Space Complexity : O(1)

# Advantages :
# It performs very well on small lists
# It is an in-place algorithm. It does not require a lot of space for sorting. 
# Only one extra space is required for holding the temporal variable.
# It performs well on items that have already been sorted.

# Disadvantages :
# It performs poorly when working on huge lists.
# The number of iterations made during the sorting is n-squared, 
# where n is the total number of elements in the list.
# Other algorithms, such as quicksort, have 
# better performance compared to the selection sort.