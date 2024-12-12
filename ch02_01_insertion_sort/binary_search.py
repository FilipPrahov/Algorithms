# The array must be sorted first, and then binary search can be applied

import math

def binarySearch(A, p, r, v):
    print("A= ", A, "; p=", p, "; r=", r, "; v=", v)
    if r > p:
        q = math.floor((r+p)/2)
        if A[q] == v:
            print("Found!")
        elif (q == p or q == r):
            print("Not found!")
        elif A[q] > v:
            binarySearch(A, p, q, v)
        else:
            binarySearch(A, q, r, v)
    else:
        print("Not found")
        
        
        
A = [-31, -27, -15, -1, 0, 3, 17, 22, 22, 28, 39, 41, 60]
binarySearch(A, 0, len(A), -50) #Not found!
binarySearch(A, 0, len(A), -31) #Found!
binarySearch(A, 0, len(A), -13) #Not found!
binarySearch(A, 0, len(A), 17)  #Found!
binarySearch(A, 0, len(A), 29)  #Not found!
binarySearch(A, 0, len(A), 60)  #Found!
binarySearch(A, 0, len(A), 170) #Not found!



