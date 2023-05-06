'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:

1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = 1+5+9 = 15. The right to left diagonal = 3+5+9 . Their absolute difference is |15-17|=2.

Function description

Complete the diagonal difference function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers
Return

int: the absolute diagonal difference
Input Format

The first line contains a single integer,n , the number of rows and columns in the square matrix arr.
Each of the next n lines describes a row, arr[i] , and consists of n space-separated integers arr[i][j].

Constraints
    -100 <= arr[i][j] <= 100

Output Format

Return the absolute difference between the sums of the matrix's two diagonals as a single integer.
'''

arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

i,j = 0,0
r_diagonals , l_diagonals = 0,0
    
while(i < len(arr)):
    while( j < len(arr[i] ) ):
        if(i==j):
            r_diagonals += arr[i][j]
            break
        j+=1
    i+=1
        
j=len(arr)-1
for i in range(len(arr)):
    for j in range(len(arr)-1,-1,-1):
        if (i+j) == (len(arr)-1):
            l_diagonals += arr[i][j]

print( abs( r_diagonals - l_diagonals))