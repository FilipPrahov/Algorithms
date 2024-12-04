// MERGE-SORT(A, p, r)
// 1 if p < r
// 2     q = lower((p + r)/2)
// 3     MERGE-SORT(A, p, q)
// 4     MERGE-SORT(A, q + 1, r)
// 5     MERGE(A, p, q, r)
// 
// MERGE(A, p, q, r)
// 1 n1 = q - p + 1
// 2 n2 = r - q
// 3 let L[1..n1+1] and R[1..n2+1] be new arrays
// 4 for i = 1 to n1
// 5     L[i]= A[p + i - 1]
// 6 for j = 1 to n2
// 7     R[j] = A[q + j]
// 8 L[n1 + 1] = inf
// 9 R[n2 + 1] = inf
// 10 i = 1
// 11 j = 1
// 12 for k = p to r
// 13    if L[i] <= R[j]
// 14        A[k] = L[i]
// 15        i = i + 1
// 16    else A[k] = R[j]
// 17        j = j + 1

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

int merge(int A[], int p, int q, int r)
{
	printArray(A, 11);
	int n1 = q - p + 1;
	//printf("n1 = %d\n", n1);
    int n2 = r - q;
	//printf("n2 = %d\n", n2);
	int L[n1+1];
	int R[n2+1];
	
	for (int i = 0; i < n1; i++){
		L[i] = A[p + i];
	}
	
	for (int j = 0; j < n2; j++){
		R[j] = A[q + j + 1];
	}
	
	//set an infinity value at the end of the array
	L[n1] = INT_MAX;
	R[n2] = INT_MAX;
	
	int i = 0;
	int j = 0;
	//printArray(L, n1);
	//printArray(R, n2);
	for (int k = p; k < r + 1; k++){
		if (L[i] <= R[j]){
			A[k] = L[i];
			i = i + 1;
		} else {
			A[k] = R[j];
			j = j + 1;
		}
	}
	//printArray(A, 11);
	return 0;
}


int mergeSort(int A[], int p, int r)
{
	if (p < r){
		int q = ((p + r)/2); //C floors the division to the lower integer
		//printf("q = %d\n", q);
        mergeSort(A, p, q);
        mergeSort(A, q + 1, r);
        merge(A, p, q, r);
	}
	return 0;
}


int main(void)
{
	int A[] = {81, 41, 59, 26, -32, 17, 41, 58, -5, 0, -13};
	mergeSort(A, 0, 10);
	printArray(A, 11);
	
	printf("\n");
	
	for (int j = 0; j < 11; j++){
		printf("%d\t", A[j]);
	}
	
	return 0;
}
