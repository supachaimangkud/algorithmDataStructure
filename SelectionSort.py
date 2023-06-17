#go through all its elements, find the smallest one, and put it in first position
#go through all its remaining elements, find the smallest one, and put it in second position
#and so on

#there are 2 pointer. One pointer is used to point to the current min which min pointer pointed to 
#the first element in the beginning and the 2nd pointer is used to find minimum
def swap(A, i, index_min):
    tmp = A[i]
    A[i] = A[index_min]
    A[index_min] = tmp 

def findMin(A, i):
    index_min = i
    for j in range(index_min + 1, len(A)):  
        #index_min + 1 because it will only have to checke from the next element to the last element
        if A[index_min] > A[j]:
            index_min = j
    
    return index_min

def selection_sort(A):
    for i in range(len(A)):
        index_min = findMin(A, i)
        swap(A, i, index_min)

    return A
A = [2,4,5,1,3,10]
print(selection_sort(A))