#insertion sort checks whether the left element(s) is greater or less than the element in
#current position
#if the element in the current position is less than the elements in the left it will insert in the beginning
#example [10,8,1,2] --> [1,8,10,2] --> [1,2,8,10]
#example [5,9,7,6]  --> [5,7,9,6] --> [5,6,7,9]


#element_1p: element from 1st pointer(from the loop in insertion_sort)
def insert(element_1p, A, index_i):
    for j in range(index_i-1, -1, -1):
        #it's used to insert the element at the first position which the element
        #isn't in the beginning of the array.
        #example [1,5,6,7,2] --> [1,2,5,6,7] "2" is in the correct position now.
        if element_1p >= A[j]:
            A[j+1] = element_1p 
            return
         
        #it's copy the element from the j position to j+1 position
        #example, assume j = 1. [5,6,1,7,2] --> [5,6,6,7,2]
        A[j+1] = A[j]

    #it will put the element in the first position if the correct position is in the beginning 
    #of the array
    #example, [5,5,6,7,2] --> [0,5,6,7,2]
    A[0] = element_1p

def insertion_sort(A):
    for i in range(1,len(A)):
        insert(A[i], A, i)

    return A

A = [5,6,1,7,2]
print(insertion_sort(A))