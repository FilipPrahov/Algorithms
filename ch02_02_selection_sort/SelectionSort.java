//  SELECTION-SORT
//  Find the min value in an array and replace it with the first value.
//  Then, go to the 2nd value and repeat
//  1 for j = 1 to A.length:
//  2    minV = A[j]
//  3    minIndex = j
//  4    for i = (j+1) to A.length:
//  5      if A[i] < minV:
//  6         minV = A[i];
//  7         minIndex = i;
//  8    if (minIndex != j):
//  9         A[minIndex] = A[j];
// 10         A[j] = minV;


import java.util.*;  


public class SelectionSort{
	// non-decreasing order selection sort algorithm
	public static void selectionSortAsc(int[] A)
	{
		int n = A.length;
		int minV, minIndex;
		
		for(int j = 0; j < n; j++){ 
			minV = A[j];
			minIndex = j;
			for (int i =j+1; i < n; i++){
				if (A[i] < minV){
					minV = A[i];
					minIndex = i;
				}
			}
			//min value and index are found, now replace with j
			if (minIndex != j){
				A[minIndex] = A[j];
				A[j] = minV;
			}
		}
		
		for (int j = 0; j < n; j++){
			System.out.print(A[j] + "\t");
		}
		System.out.println();
	}
	
	
	// non-increasing order insertion sort algorithm
	public static void selectionSortDesc(int[] A)
	{
		int n = A.length;
		int maxV, maxIndex;
		
		for(int j = 0; j < n; j++){ 
			maxV = A[j];
			maxIndex = j;
			for (int i =j+1; i < n; i++){
				if (A[i] > maxV){
					maxV = A[i];
					maxIndex = i;
				}
			}
			//min value and index are found, now replace with j
			if (maxIndex != j){
				A[maxIndex] = A[j];
				A[j] = maxV;
			}
		}
		
		for (int j = 0; j < n; j++){
			System.out.print(A[j] + "\t");
		}
		System.out.println();
	}
	
	
	public static void main(String[] s)
	{
		int[] A = {31, 41, 59, 26, -32, 41, 58, -5, 0, -13};
		selectionSortAsc(A);
		selectionSortDesc(A);
	}
}