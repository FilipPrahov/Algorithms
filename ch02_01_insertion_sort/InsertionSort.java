//  INSERTION-SORT.A/
//  1 for j = 2 to A.length
//  2    key = A[j]
//  3    // Insert A[j] into the sorted sequence A[1..j-1].
//  4    i = j - 1
//  5    while i > 0 and A[i] > key
//  6        A[i+1] = A[i]
//  7        i = i - 1
//  8    A[i+1] = key

import java.util.*;  

public class InsertionSort {
	public static void insertionSortAsc(int[] A){
		int key, i;
		int n = A.length;
		// non-decreasing order insertion sort algorithm
		for (int j = 1; j < n; j++){
			key = A[j];
			i = j - 1;
			while (i >= 0 && A[i] > key){
				A[i+1] = A[i];
				i = i - 1;
			}
			A[i+1] = key;
		}
		for (int j = 0; j < n; j++){
			System.out.print(A[j] + "\t");
		}
		System.out.println();
	}
	
	public static void insertionSortDesc(int[] A){
		int key, i;
		int n = A.length;
		// non-increasing order insertion sort algorithm
		for (int j = 1; j < n; j++){
			key = A[j];
			i = j - 1;
			while (i >= 0 && A[i] < key){
				A[i+1] = A[i];
				i = i - 1;
			}
			A[i+1] = key;
		}
		for (int j = 0; j < n; j++){
			System.out.print(A[j] + "\t");
		}
		System.out.println();
	}
	
	public static void main(String[] s){
		int[] A = {31, 41, 59, 26, 41, 58};
		insertionSortAsc(A);
		insertionSortDesc(A);
	}
}