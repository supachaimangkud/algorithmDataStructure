def mergeSort(A):
    if len(A) <= 1:
        return
    mid = len(A)//2
    half1 = A[:mid]
    half2 = A[mid:]
    mergeSort(half1)
    mergeSort(half2)
    merge(half1,half2,A)

    return A


def merge(half1, half2, A):
    #it is used as an index for replacing element from half1 or half2 in array A
    #i, j1, j2 are incremented by 1 everytime it is used
    i=0    
    j1=0
    j2=0
    
    #this loop is used for sorting and put element in A
    while j1<len(half1) and j2<len(half2):
        if half1[j1] < half2[j2]:
            A[i] = half1[j1]
            j1 += 1
            i += 1
        else:
            A[i] = half2[j2]
            j2 += 1
            i += 1
    
    #the last 2 loops are used to put the remain element from half1 or half2 in array A.
    #for example, the last element(the largest int)
    while j1 < len(half1):
        A[i] = half1[j1]
        j1 += 1
        i += 1
    while j2 < len(half2):
        A[i] = half2[j2]
        j2 += 1
        i += 1


A = [7,2,3,1,10,9]
print(mergeSort(A))
