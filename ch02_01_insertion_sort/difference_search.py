# The array must be sorted first, and then binary search can be applied

import math

def binarySearch(A, p, r, v):
    print("A= ", A, "; p=", p, "; r=", r, "; v=", v)
    if r > p:
        q = math.floor((r+p)/2)
        if A[q] == v:
            print("Found!")
            searchResult = True
        elif (q == p or q == r):
            print("Not found!")
        elif A[q] > v:
            binarySearch(A, p, q, v)
        else:
            binarySearch(A, q, r, v)
    else:
        print("Not found")
        
    if searchResult:
        return True
    else:
        return False
        
        
        
A = [-31, -27, -15, -1, 0, 3, 17, 22, 22, 28, 39, 41, 60]
#binarySearch(A, 0, len(A), -50) #Not found!
#binarySearch(A, 0, len(A), -31) #Found!
#binarySearch(A, 0, len(A), -13) #Not found!
#binarySearch(A, 0, len(A), 17)  #Found!
#binarySearch(A, 0, len(A), 29)  #Not found!
#binarySearch(A, 0, len(A), 60)  #Found!
#binarySearch(A, 0, len(A), 170) #Not found!


# Task 2.3-7: 
#Describe a theta(n lg n)-time algorithm that, given a set S of n integers and another
#integer x, determines whether or not there exist two elements in S whose sum is
#exactly x.

#Solution: binary search is theta(ld n) algorithm. 
#For each element in S, calculate the difference d = (x - S[j]) and check if d in S via 
#binary search. This algorithm executes binary search n times, therefore it is theta(n lg n)-time algorithm

x = 50
found = False

for i in range(0, len(A)):
    d = x - A[i]
    found = binarySearch(A, 0, len(A), d)
    if (found):
        print("The sum is possible")
    
