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

import java.util.*;  



public class MaxSubarrayAlgo{
	public static void printArray(int A[])
	{
		for (int j = 0; j < A.length; j++){
			System.out.print(A[j] + "\t");
		}
		System.out.println();
	}
	

	
	public ResultTuple findMaxCrossingSubarray(int A[], int low, int mid, int high)
	{
		int leftSum = Integer.MIN_VALUE;;
		int sum = 0;
		int maxLeft = -1;
		
		for (int i = mid; i>= low; i--){
			sum += A[i];
			if (sum > leftSum){
				leftSum = sum;
				maxLeft = i;
			}
		}
		
		int rightSum = Integer.MIN_VALUE;
		sum = 0;
		int maxRight = -1;
		
		for (int j = mid+1; j<= high; j++){
			sum += A[j];
			if (sum > rightSum){
				rightSum = sum;
				maxRight = j;
			}
		}
		
		ResultTuple resultCross = new ResultTuple(maxLeft, maxRight, (leftSum + rightSum));
		//resultCross = (maxLeft, maxRight, (leftSum + rightSum));
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
	
	public ResultTuple findMaximumSubarray(int A[], int low, int high){
		if (high == low){ 
			ResultTuple  resultOneElem = new ResultTuple(low, high, A[low]);
			//resultOneElem = {low, high, A[low] };
			return resultOneElem;          // base case: only one element
		} else {
			int mid = ((low + high)/2);
			
			ResultTuple  resultLeft = new ResultTuple(-1, -1, Integer.MIN_VALUE);
			resultLeft = findMaximumSubarray(A, low, mid);
			
			ResultTuple  resultRight = new ResultTuple(-1, -1, Integer.MIN_VALUE);
			resultRight = findMaximumSubarray(A, mid + 1, high);
			
			ResultTuple  resultAcross = new ResultTuple(-1, -1, Integer.MIN_VALUE);
			resultAcross = findMaxCrossingSubarray(A, low, mid, high);
	
			if (resultLeft.subArrSum >= resultRight.subArrSum && resultLeft.subArrSum >= resultAcross.subArrSum){
				System.out.println(resultLeft.toString());
				return resultLeft;
			} else if (resultRight.subArrSum >= resultLeft.subArrSum && resultRight.subArrSum >= resultAcross.subArrSum) {
				System.out.println(resultRight.toString());
				return resultRight;
			} else {
				System.out.println(resultAcross.toString());
				return resultAcross;
			}
		}
	}
			
	public static void main(String[] args){
			int A[] = {9, -12, 5, -12, 26, 3, -8, 17, 2, 6, 13, -7, 10, -15, 3, -2};
			
			MaxSubarrayAlgo maxArrayResult = new MaxSubarrayAlgo();
			maxArrayResult.findMaximumSubarray(A, 0, A.length-1);
	}
}

	class ResultTuple
	{
		int leftIndex;
		int rightIndex;
		int subArrSum;
		
		ResultTuple(int leftIndex, int rightIndex, int subArrSum){
			this.leftIndex = leftIndex;
			this.rightIndex = rightIndex;
			this.subArrSum = subArrSum;
		}
		
		public String toString(){
			return "Low = " + this.leftIndex + ", High = " + this.rightIndex + ", Sum = " + this.subArrSum;
		}
	};
