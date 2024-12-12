// The algorithm searches for a sub-array with max sum
//
// FIND-MAX-CROSSING-SUBARRAY(A; low; mid; high)
// 1     left-sum = -inf
// 2     sum = 0
// 3     for i = mid downto low:
// 4         sum = sum + A[i]
// 5         if sum > left-sum:
// 6             left-sum = sum
// 7             max-left = i
// 8     right-sum = -inf
// 9     sum = 0
// 10    for j = mid + 1 to high:
// 11        sum = sum + A[j]
// 12        if sum > right-sum:
// 13            right-sum = sum
// 14            max-right = j
// 15    return (max-left; max-right; left-sum + right-sum)


#include <stdio.h>
#include <limits.h>

int printArray(int A[], int n)
{
	for (int j = 0; j < n; j++){
		printf("%d\t", A[j]);
	}
	printf("\n");
	return 0;
}

struct resultTuple
{
	int leftIndex;
	int rightIndex;
	int subArrSum;
};

struct resultTuple findMaxCrossingSubarray(int A[], int low, int mid, int high)
{
	int leftSum = INT_MIN;
	int sum = 0;
	int maxLeft = -1;
	
	for (int i = mid; i>= low; i--){
		sum += A[i];
		if (sum > leftSum){
			leftSum = sum;
			maxLeft = i;
		}
	}
	
	int rightSum = INT_MIN;
	sum = 0;
	int maxRight = -1;
	
    for (int j = mid+1; j<= high; j++){
		sum += A[j];
		if (sum > rightSum){
			rightSum = sum;
			maxRight = j;
		}
	}
	
	struct resultTuple resultCross = {maxLeft, maxRight, leftSum + rightSum };
	return resultCross;
}


// FIND-MAXIMUM-SUBARRAY(A; low; high)
// 1 if high == low:
// 2     return (low; high;A[l])          // base case: only one element
// 3 else mid = floor((low + high)/2)
// 4     (left-low; left-high; left-sum) = FIND-MAXIMUM-SUBARRAY(A; low; mid)
// 5     (right-low; right-high; right-sum) = FIND-MAXIMUM-SUBARRAY(A; mid + 1; high)
// 6     (cross-low; cross-high; cross-sum) = FIND-MAX-CROSSING-SUBARRAY(A; low; mid; high)
// 7     if left-sum >= right-sum and left-sum >= cross-sum:
// 8         return (left-low; left-high; left-sum)
// 9     elseif right-sum >= left-sum and right-sum >= cross-sum:
// 10        return (right-low; right-high; right-sum)
// 11    else return (cross-low; cross-high; cross-sum)

struct resultTuple findMaximumSubarray(int A[], int low, int high){
    if (high == low){ 
		struct resultTuple resultOneElem = {low, high, A[low] };
        return resultOneElem;          // base case: only one element
	} else {
        int mid = ((low + high)/2);
        
		struct resultTuple resultLeft = findMaximumSubarray(A, low, mid);
        struct resultTuple resultRight = findMaximumSubarray(A, mid + 1, high);
		struct resultTuple resultAcross = findMaxCrossingSubarray(A, low, mid, high);

		if (resultLeft.subArrSum >= resultRight.subArrSum && resultLeft.subArrSum >= resultAcross.subArrSum){
			return resultLeft;
		} else if (resultRight.subArrSum >= resultLeft.subArrSum && resultRight.subArrSum >= resultAcross.subArrSum) {
			return resultRight;
		} else {
			return resultAcross;
		}
	}
}
        
int main(void){
		int A[] = {9, -12, 5, -12, 26, 3, -8, 17, 2, 6, 13, -7, 10, -15, 3, -2};
		// variable to store size of Array A
		int length = sizeof(A) / sizeof(A[0]);
		struct resultTuple maxArrayResult = findMaximumSubarray(A, 0, length-1);
		
		printf("Low = %d, High = %d, Sum = %d", maxArrayResult.leftIndex, maxArrayResult.rightIndex, maxArrayResult.subArrSum);
}


