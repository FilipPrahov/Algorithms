// SQUARE-MATRIX-MULTIPLY.A;B/
// 1 n = A.rows
// 2 let C be a new n*n matrix
// 3 for i = 1 to n
// 4     for j = 1 to n
// 5         c[i][j] = 0
// 6         for k = 1 to n
// 7             c[i][j] = c[i][j] + a[i][k] * b[k][j]
// 8 return C

#include <stdio.h>
#include <limits.h>

int print2DSqArray(int n, int A[n][n])
{
	for (int j = 0; j < n; j++){
		for (int i = 0; i < n; i++){
			printf("%d\t", A[j][i]);
		}
		printf("\n");
	}
	printf("\n");
	return 0;
}

int matrixMultiply(int n, int A[n][n],int B[n][n],int C[n][n]){
	for (int i = 0; i < n; i++){
		for (int j = 0; j < n; j++){
			C[i][j] = 0;
			for (int k = 0; k < n; k++){
				C[i][j] = C[i][j] + A[i][k] * B[k][j];
			}
		}
	}
	return 0;
}

    
int main(void)
{
	int A[3][3] = {{1,2,3},{4,5,6},{7,8,9}};
	int B[3][3] = {{-1,-2,-3},{-4,-5,-6},{-7,-8,-9}};
	int C[3][3] = {{INT_MIN, INT_MIN, INT_MIN},{INT_MIN, INT_MIN, INT_MIN},{INT_MIN, INT_MIN, INT_MIN}};
	
	int lenA = sizeof(A)/sizeof(A[0]);
	int lenB = sizeof(B)/sizeof(B[0]);
	int lenC = sizeof(C)/sizeof(C[0]);
	
	if (lenA == lenB && lenA == lenC){
		matrixMultiply(lenA, A, B, C);
		print2DSqArray(lenC, C);
	} else {
		printf("Matrix sizes are not equal - cannot multiply");
	}
	

}