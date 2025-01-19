import math

A = [9, -12, 5, -12, 26, 3, -8, 17, 2, 6, 13, -7, 10, -15, 3, -2]

totalSum = -math.inf
leftIndex = 0
rightIndex = len(A) - 1

#(a,b,c) = findMaximumSubarray(A, 0, len(A)-1)
#print("Low = ", a, "; High = ", b, "; Max sum = ", c)

for j in range(0, len(A)):
    for i in range(len(A), j, -1):
        runningSum = sum(A[slice(j,i)])
        if (totalSum < runningSum):
            print(runningSum)
            totalSum = runningSum
            leftIndex = j
            rightIndex = i-1  #subtract 1 because slice function takes up-to-but-without the end index 

print("Low = ", leftIndex, "; High = ", rightIndex, "; Sum = ", totalSum)