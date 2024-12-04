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


#include <iostream>
using namespace std;



// non-decreasing order selection sort algorithm
int selection_sort_asc(int A[], int n)
{
	for(int j = 0; j < n; j++){ 
		int minV = A[j];
		int minIndex = j;
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
		cout << A[j] << '\t';
	}
	return 0;
}


// non-increasing order insertion sort algorithm
int selection_sort_desc(int A[], int n)
{
	for(int j = 0; j < n; j++){ 
		int maxV = A[j];
		int maxIndex = j;
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
		cout << A[j] << '\t';
	}
	return 0;
}


int main(void)
{
	int A[10] = {31, 41, 59, 26, -32, 41, 58, -5, 0, -13};
	selection_sort_asc(A, 10);
	cout << '\n';
	selection_sort_desc(A, 10);

	return 0;
}