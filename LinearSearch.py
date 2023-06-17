def search(A, v):
    found = -1
    
    for i in range(len(A)):
        if A[i] == v:
            found = 1
    
    return found

A = [2,1,3,4,7,8]
v = 2

print(search(A, v))
#O(n) because it has to go through every element. n loops
