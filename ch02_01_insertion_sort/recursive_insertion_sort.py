import time

def insertStep(A, p, r):
    #first r-1 elements are sorted, insert the nth element
    key = A[r-1]
    i = r-2
    while i >= 0 and A[i] > key:
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key
    #print("return from insertStep")


    
    
# non-decreasing order insertion sort algorithm
def recursiveInsertionSort(A, p, r):
    print("A= ", A, "; p=", p, "; r=", r)
    #time.sleep(1)
    if r > 2:
        recursiveInsertionSort(A, 0, r-1)
    insertStep(A, p, r)
    
    

A = [81, 41, 59, 26, 41, -13, 58]
recursiveInsertionSort(A, 0, len(A))

print(A)