# SQUARE-MATRIX-MULTIPLY-RECURSIVE.A;B/
# 1 n = A.rows
# 2 let C be a new n*n matrix
# 3 if n == 1
# 4     c11 = a11 * b11
# 5 else partition A, B, and C as in equations (4.9)
# 6     C11 = SQUARE-MATRIX-MULTIPLY-RECURSIVE(A11;B11)
#       + SQUARE-MATRIX-MULTIPLY-RECURSIVE(A12,B21)
# 7     C12 = SQUARE-MATRIX-MULTIPLY-RECURSIVE(A11,B12)
#       + SQUARE-MATRIX-MULTIPLY-RECURSIVE(A12,B22)
# 8     C21 = SQUARE-MATRIX-MULTIPLY-RECURSIVE(A21,B11)
#       + SQUARE-MATRIX-MULTIPLY-RECURSIVE(A22,B21)
# 9     C22 = SQUARE-MATRIX-MULTIPLY-RECURSIVE(A21,B12)
#      + SQUARE-MATRIX-MULTIPLY-RECURSIVE(A22,B22)
# 10 return C


import math
import numpy as np

def binaryMatrixMultiplyRecursive(A, B):
    n = len(A)
    C = np.array([[0 for x in range(n)] for y in range(n)])
    if (n == 1):
        C[0][0] = A[0][0]*B[0][0]
        #return C[0][0]
    else:
        C[0:int(n/2), 0:int(n/2)] = binaryMatrixMultiplyRecursive(A[0:int(n/2), 0:int(n/2)], B[0:int(n/2), 0:int(n/2)]) \
            + binaryMatrixMultiplyRecursive(A[0:int(n/2), int(n/2):n], B[int(n/2):n, 0:int(n/2)])
        C[0:int(n/2), int(n/2):n] = binaryMatrixMultiplyRecursive(A[0:int(n/2), 0:int(n/2)], B[0:int(n/2), int(n/2):n]) \
            + binaryMatrixMultiplyRecursive(A[0:int(n/2), int(n/2):n], B[int(n/2):n, int(n/2):n])
        C[int(n/2):n, 0:int(n/2)] = binaryMatrixMultiplyRecursive(A[int(n/2):n, 0:int(n/2)], B[0:int(n/2), 0:int(n/2)]) \
            + binaryMatrixMultiplyRecursive(A[int(n/2):n, int(n/2):n], B[int(n/2):n, 0:int(n/2)])
        C[int(n/2):n, int(n/2):n] = binaryMatrixMultiplyRecursive(A[int(n/2):n, 0:int(n/2)], B[0:int(n/2), int(n/2):n]) \
            + binaryMatrixMultiplyRecursive(A[int(n/2):n, int(n/2):n], B[int(n/2):n, int(n/2):n])
    #print(C)
    return C


A = np.array([[-1,2,-3,4],[-5,6,-7, 8],[-9, 10, -11, 12],[0, 1, 0 , 1]])
B = np.array([[1,-2,3, -4],[5,-6, 7, -8],[9, -10, 11, -12], [0, -1, 0, -1]])

print(binaryMatrixMultiplyRecursive(A, B))
#print(A[0 : int(n/2),0 : int(n/2)])
#print(A)
