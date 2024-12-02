#  INSERTION-SORT.A/
#  1 for j = 2 to A.length
#  2    key = A[j]
#  3    // Insert A[j] into the sorted sequence A[1..j-1].
#  4    i = j - 1
#  5    while i > 0 and A[i] > key
#  6        A[i+1] = A[i]
#  7        i = i - 1
#  8    A[i+1] = key

A = [31, 41, 59, 26, 41, 58]

# non-decreasing order insertion sort algorithm
for j in range(1, len(A)):
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] > key:
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key

print(A)

# non-increasing order insertion sort algorithm
for j in range(1, len(A)):
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] < key:
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key

print(A)