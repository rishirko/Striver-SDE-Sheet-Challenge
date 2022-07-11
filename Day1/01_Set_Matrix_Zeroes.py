#Rishi's Solution
#...
# select the first row and first col as dummy array.
# now traverse the whole matrix, starting from the 2nd row and 2nd col, 
# and whenever you get a zero(i.e, matrix[i][j]==0), mark the row and col number as zero in the dummy arrays.
# now traverse the matrix again and check those dummy arrays, if you get any zero, the mark matrix[i][j]=0.
# at last check if 1st row or col had zero and change it accordingly.
                                                                                      

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_in_first_row=False
        zero_in_first_col=False
        
        n=len(matrix)
        m=len(matrix[0])
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    if i==0:
                        zero_in_first_row=True
                    if j==0:
                        zero_in_first_col=True
                    matrix[0][j]=0
                    matrix[i][0]=0
                    
        for i in range(1,n):
            for j in range(1,m):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
        if zero_in_first_row:
            for j in range(m):
                matrix[0][j]=0
                
        if zero_in_first_col:
            for i in range(n):
                matrix[i][0]=0
