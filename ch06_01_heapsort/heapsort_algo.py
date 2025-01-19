import math


#PARENT(i)
# return floor(i/2)
#LEFT(i) 
# return 2*i
#RIGHT(i)
# return 2*i + 1

#N.B. Lists are 0-based in Python so some adjustment is required
def parent(i):
    return (i+1)//2 - 1

def left(i):
    return 2*i + 1
    
def right(i):
    return 2*i + 2



#   In order to maintain the max-heap property, we call the procedure MAX-HEAPIFY.
#   Its inputs are an array A and an index i into the array. When it is called, MAX-HEAPIFY
#   assumes that the binary trees rooted at LEFT(i) and RIGHT(i) are maxheaps,
#   but that A[i] might be smaller than its children, thus violating the max-heap
#   property. MAX-HEAPIFY lets the value at A[i] “float down” in the max-heap so
#   that the subtree rooted at index i obeys the max-heap property.
#


#   MAX-HEAPIFY(A, i)
#   1 l = LEFT(i)
#   2 r = RIGHT(i)
#   3 if l <= A.heap-size and A[l] > A[i]
#   4   largest = l
#   5 else largest = i
#   6 if r <= A.heap-size and A[r] > A[largest]
#   7   largest = r
#   8 if largest != i
#   9   exchange A[i] with A[largest]
#   10  MAX-HEAPIFY(A, largest)

def maxHeapify(A, i):
    print(A)
    l = left(i)
    r = right(i)
    if l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, largest)
        



# We can use the procedure MAX-HEAPIFY in a bottom-up manner to convert an
# array A[1..n], where n = A.length, into a max-heap. By Exercise 6.1-7, the
# elements in the subarray A[(n/2+1).. n] are all leaves of the tree, and so each is
# a 1-element heap to begin with. The procedure BUILD-MAX-HEAP goes through
# the remaining nodes of the tree and runs MAX-HEAPIFY on each one.
# BUILD-MAX-HEAP(A)
# 1 A.heap-size = A.length
# 2 for i = (A.length/2) downto 1
# 3     MAX-HEAPIFY(A,i)

def buildMaxHeap(A):
    for i in range(len(A)//2-1, -1, -1):
        print(i)
        maxHeapify(A, i)



# The heapsort algorithm starts by using BUILD-MAX-HEAP to build a max-heap
# on the input array A[1..n], where n = A.length. Since the maximum element
# of the array is stored at the root A[1], we can put it into its correct final position
# by exchanging it with A[n]. If we now discard node n from the heap — and we
# can do so by simply decrementing A.heap-size — we observe that the children of
# the root remain max-heaps, but the new root element might violate the max-heap
# property. All we need to do to restore the max-heap property, however, is call
# MAX-HEAPIFY[A, 1], which leaves a max-heap in A[1..n - 1]. The heapsort
# algorithm then repeats this process for the max-heap of size n = 1 down to a heap
# of size 2.
# 
# 
# HEAPSORT(A)
# 1 BUILD-MAX-HEAP(A)
# 2 for i = A:length downto 2
# 3     exchange A[1] with A[i]
# 4     A.heap-size = A.heap-size - 1
# 5     MAX-HEAPIFY(A, 1)


def heapsort(A):
    buildMaxHeap(A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        Asorted.append(A[-1])
        A = A[:-1]
        maxHeapify(A, 0)
    print(Asorted)

#############################################################################
###############  PRIORITY QUEUES IMPLEMENTATION  ############################
#############################################################################

# A priority queue is a data structure for maintaining a set S of elements, each
# with an associated value called a **key**. A max-priority queue supports 
# the following operations:
# INSERT(S,x) inserts the element x into the set S, which is equivalent to 
# the operation S = S U {x}  Runs in O(lg n) time
# MAXIMUM(S) returns the element of S with the largest key. Runs is Theta(1) time
# EXTRACT-MAX(S) removes and returns the element of S with the largest key. Runs in O(lg n) time
# INCREASE-KEY(S, x, k) increases the value of element x’s key to the new value k,
# which is assumed to be at least as large as x’s current key value. Runs in O(lg n) time

# HEAP-MAXIMUM(A):
# 1 return A[1]

def heapMaximum(A):
    return A[0]
    

# HEAP-EXTRACT-MAX(A):
# 1 if A.heap-size < 1
# 2     error “heap underflow”
# 3 max = A[1]
# 4 A[1] = A[A.heap-size]
# 5 A.heap-size = A.heap-size - 1
# 6 MAX-HEAPIFY(A, 1)
# 7 return max

def heapExtractMax(A):
    if len(A) < 1:
        raise NameError('heap underflow')
    maxElem = A[0]
    A[0] = A[len(A)-1]
    A = A[:-1]
    maxHeapify(A, 0)
    return maxElem, A
    
    
# HEAP-INCREASE-KEY(A, i, key)
# 1 if key < A[i]
# 2     error “new key is smaller than current key”
# 3 A[i] = key
# 4 while i > 1 and A[PARENT(i)] < A[i]
# 5     exchange A[i] with A[PARENT(i)]
# 6     i = PARENT[i]

def heapIncreaseKey(A, i, key):
    if key < A[i]:
        raise NameError('new key is smaller than current key')
    A[i] = key
    while i > 0 and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


# MAX-HEAP-INSERT(A, key)
# 1 A.heap-size = A.heap-size + 1
# 2 A[A.heap-size] = -inf
# 3 HEAP-INCREASE-KEY(A,A.heap-size, key)

def maxHeapInsert(A, key):
    A.append(-math.inf)
    heapIncreaseKey(A, len(A)-1, key)


#test
A = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
maxHeapify(A, 2)


#test 2
B = [5, 3, 17, 10, 84, 19, 6, 22, 9]
buildMaxHeap(B)


#test 3
C = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
Asorted = []
heapsort(C)

#test 4
print("############## priority queue test ###############")
D = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
buildMaxHeap(D)
currMaxElem = heapMaximum(D)
print(currMaxElem)
currMaxElem, D = heapExtractMax(D)
print(currMaxElem)
maxHeapInsert(D, 47)
maxHeapInsert(D, 4)
maxHeapInsert(D, 2)
print(D)
while (len(D)>0):
    print("D contains ", len(D), " elements")
    currMaxElem, D = heapExtractMax(D)
    print(currMaxElem)