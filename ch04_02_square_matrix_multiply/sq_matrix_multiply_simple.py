# SQUARE-MATRIX-MULTIPLY.A;B/
# 1 n = A.rows
# 2 let C be a new n*n matrix
# 3 for i = 1 to n
# 4     for j = 1 to n
# 5         c[i][j] = 0
# 6         for k = 1 to n
# 7             c[i][j] = c[i][j] + a[i][k] * b[k][j]
# 8 return C

import math
import numpy as np

def matrixMultiply(A, B, C):
    n = len(A)
    print(n)
    for i in range(0,n):
        for j in range(0,n):
            C[i][j] = 0
            for k in range(0, n):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]
    return C

    

A = np.array([[-1,2,-3,4],[-5,6,-7, 8],[-9, 10, -11, 12],[0, 1, 0 , 1]])
B = np.array([[1,-2,3, -4],[5,-6, 7, -8],[9, -10, 11, -12], [0, -1, 0, -1]])
C = [[0 for x in range(4)] for y in range(4)]
C = matrixMultiply(A, B, C)
print(C)