# The algorithm searches for a sub-array with max sum

# FIND-MAX-CROSSING-SUBARRAY(A; low; mid; high)
# 1     left-sum = -inf
# 2     sum = 0
# 3     for i = mid downto low:
# 4         sum = sum + A[i]
# 5         if sum > left-sum:
# 6             left-sum = sum
# 7             max-left = i
# 8     right-sum = -inf
# 9     sum = 0
# 10    for j = mid + 1 to high:
# 11        sum = sum + A[j]
# 12        if sum > right-sum:
# 13            right-sum = sum
# 14            max-right = j
# 15    return (max-left; max-right; left-sum + right-sum)
import math

def findMaxCrossingSubarray(A, low, mid, high):
    #print(A, low, mid, high)
    leftSum = -math.inf
    sum = 0
    for i in range(mid, low-1, -1):
        sum = sum + A[i]
        #print(sum)
        if sum > leftSum:
            leftSum = sum
            #print(leftSum)
            maxLeft = i
            #print(maxLeft)
    rightSum = -math.inf
    sum = 0
    for j in range(mid+1, high+1):
        sum = sum + A[j]
        if sum > rightSum:
            rightSum = sum
            maxRight = j
    #print(maxLeft)        
    return (maxLeft, maxRight, leftSum + rightSum)


# FIND-MAXIMUM-SUBARRAY(A; low; high)
# 1 if high == low:
# 2     return (low; high;A[l])          // base case: only one element
# 3 else mid = floor((low + high)/2)
# 4     (left-low; left-high; left-sum) = FIND-MAXIMUM-SUBARRAY(A; low; mid)
# 5     (right-low; right-high; right-sum) = FIND-MAXIMUM-SUBARRAY(A; mid + 1; high)
# 6     (cross-low; cross-high; cross-sum) = FIND-MAX-CROSSING-SUBARRAY(A; low; mid; high)
# 7     if left-sum >= right-sum and left-sum >= cross-sum:
# 8         return (left-low; left-high; left-sum)
# 9     elseif right-sum >= left-sum and right-sum >= cross-sum:
# 10        return (right-low; right-high; right-sum)
# 11    else return (cross-low; cross-high; cross-sum)


def findMaximumSubarray(A, low, high):
    if high == low: # or (high - low) == 1:
        return (low, high, A[low])          # base case: only one element
    else:
        mid = math.floor((low + high)/2)
        print("Low = ", low, "; Mid = ", mid, "; High = ", high, "; A = ", A)
        (leftLow, leftHigh, leftSum) = findMaximumSubarray(A, low, mid)
        print("leftLow = ", leftLow,"; leftHigh = ", leftHigh,"; leftSum = ", leftSum)
        (rightLow, rightHigh, rightSum) = findMaximumSubarray(A, mid + 1, high)
        print("rightLow = ", rightLow,"; rightHigh = ", rightHigh,"; rightSum = ", rightSum)
        print("Call to findMaxCrossingSubarray: low = ", low, "; mid = ", mid, "; high = ", high)
        (crossLow, crossHigh, crossSum) = findMaxCrossingSubarray(A, low, mid, high)
        print("crossLow = ", crossLow,"; crossHigh = ", crossHigh,"; crossSum = ", crossSum)
        if leftSum >= rightSum and leftSum >= crossSum:
            return (leftLow, leftHigh, leftSum)
        elif rightSum >= leftSum and rightSum >= crossSum:
            return (rightLow, rightHigh, rightSum)
        else:
            return (crossLow, crossHigh, crossSum)
        
        

A = [9, -12, 5, -12, 26, 3, -8, 17, 2, 6, 13, -7, 10, -15, 3, -2]
(a,b,c) = findMaximumSubarray(A, 0, len(A)-1)
print("Low = ", a, "; High = ", b, "; Max sum = ", c)
