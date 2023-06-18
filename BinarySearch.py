#Concept
#We look at the middle element of A.
#If it is equal to v, we stop. Otherwise:
#if element in the middle is greater than v, we repeat the search only on the
#elements before the middle one;
#if element in the middle is less than v, we repeat the search only on the items
#after it.
#Return -1 when the range we search is of size 0.

#Binary search has to 3 pointers. lo, hi, and middle.
def binary_search(A, v):
    hi = len(A) - 1
    lo = 0
    
    #when lo > hi, it means there v is not in A
    while lo <= hi:
        #// to get lowewr bound. For example, 9//2 = 4. 4th element is in the middle of A.
        #Dont forget that first element is index 0
        mid = (hi+lo)//2     
        if A[mid] == v:
            return mid
        elif A[mid] > v:
            hi = mid - 1
        else:
            lo = mid + 1
    
    #return -1 when v is not found in A
    return -1

A = [1,4,7,10,12,14]
v = 10
print(binary_search(A, v))