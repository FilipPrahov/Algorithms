# MERGE-SORT(A, p, r)
# 1 if p < r
# 2     q = lower((p + r)/2)
# 3     MERGE-SORT(A, p, q)
# 4     MERGE-SORT(A, q + 1, r)
# 5     MERGE(A, p, q, r)
# 
# MERGE(A, p, q, r)
# 1 n1 = q - p + 1
# 2 n2 = r - q
# 3 let L[1..n1+1] and R[1..n2+1] be new arrays
# 4 for i = 1 to n1
# 5     L[i]= A[p + i - 1]
# 6 for j = 1 to n2
# 7     R[j] = A[q + j]
# 8 L[n1 + 1] = inf
# 9 R[n2 + 1] = inf
# 10 i = 1
# 11 j = 1
# 12 for k = p to r
# 13    if L[i] <= R[j]
# 14        A[k] = L[i]
# 15        i = i + 1
# 16    else A[k] = R[j]
# 17        j = j + 1

import math

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    for i in range(1, n1 + 1):
        L.append(A[p + i - 1]) 
    
    for j in range(0, n2):
        R.append(A[q + j + 1])

    L.append(math.inf)
    R.append(math.inf)
    i = j = 0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1


def mergeSort(A, p, r):
    if (p < r):
        q = math.floor((p + r)/2)
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)


A = [81, 41, 59, 26, -32, 17, 41, 58, -5, 0, -13]
mergeSort(A, 0, len(A)-1)
print(A)
