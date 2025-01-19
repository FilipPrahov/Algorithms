// SQUARE-MATRIX-MULTIPLY.A;B/
// 1 n = A.rows
// 2 let C be a new n*n matrix
// 3 for i = 1 to n
// 4     for j = 1 to n
// 5         c[i][j] = 0
// 6         for k = 1 to n
// 7             c[i][j] = c[i][j] + a[i][k] * b[k][j]
// 8 return C

#include <climits>
#include <iostream>
using namespace std;

const int row = 3, col = 3;

int print2DSqArray(const int A[row][col] )
{
	for (int j = 0; j < row; j++){
		for (int i = 0; i < col; i++){
			cout<< "\t" << A[j][i];
		}
		cout << "\n";
	}
	cout << "\n";
	return 0;
}

int matrixMultiply(const int A[row][col], const int B[row][col], int C[row][col]){
	for (int i = 0; i < row; i++){
		for (int j = 0; j < col; j++){
			C[i][j] = 0;
			for (int k = 0; k < row; k++){
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
		matrixMultiply(A, B, C);
		print2DSqArray( C );
	} else {
		cout << "Matrix sizes are not equal - cannot multiply" << endl;
	}
	

}