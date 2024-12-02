//  INSERTION-SORT.A/
//  1 for j = 2 to A.length
//  2    key = A[j]
//  3    // Insert A[j] into the sorted sequence A[1..j-1].
//  4    i = j - 1
//  5    while i > 0 and A[i] > key
//  6        A[i+1] = A[i]
//  7        i = i - 1
//  8    A[i+1] = key

#include <stdio.h>

int insertion_sort(int A[], int n){
	int key, i;
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
		printf("%d\t", A[j]);
	}
	
	printf("\n\n");
	
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
		printf("%d\t", A[j]);
	}
}

int main(void) 
{
	int A[6] = {31, 41, 59, 26, 41, 58};
	insertion_sort(A, 6);


}