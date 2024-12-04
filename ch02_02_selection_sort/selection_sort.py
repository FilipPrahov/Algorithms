#  SELECTION-SORT
#  Find the min value in an array and replace it with the first value.
#  Then, go to the 2nd value and repeat
#  1 for j = 1 to A.length:
#  2    minV = A[j]
#  3    minIndex = j
#  4    for i = (j+1) to A.length:
#  5      if A[i] < minV:
#  6         minV = A[i];
#  7         minIndex = i;
#  8    if (minIndex != j):
#  9         A[minIndex] = A[j];
# 10         A[j] = minV;


A = [31, 41, 59, 26, -32, 41, 58, -5, 0, -13]


# non-decreasing order selection sort algorithm
for j in range(0, len(A)):
    minV = A[j]
    minIndex = j
    for i in range (j+1, len(A)):
      if (A[i] < minV):
        minV = A[i]
        minIndex = i;
    #min value and index are found, now replace with j
    if (minIndex != j):
        A[minIndex] = A[j]
        A[j] = minV

print(A)

# non-increasing order insertion sort algorithm
for j in range(0, len(A)):
    maxV = A[j]
    maxIndex = j
    for i in range (j+1, len(A)):
      if (A[i] > maxV):
        maxV = A[i]
        maxIndex = i;
    #max value and index are found, now replace with j
    if (maxIndex != j):
        A[maxIndex] = A[j]
        A[j] = maxV

print(A)