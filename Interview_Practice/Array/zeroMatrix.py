"""
Given a matrix if an element in the matrix is 0 then you will have to set its entire 
column and row to 0 and then return the matrix.

clarifying questions : 
what if the matrics is null.
does the number of rows equals to no. of columns? : so, we need to calculate n and m

any negatives or -1?

brute force : 

traverse through array, and mark -1 to all rows and columns as -1 wherewher we find zero,
except that zero :

then traverse throgh matrics again, and mark 0 wherewher there is -1

"""
def markRow(matrix, m , i):
    for j in range(m):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def markCol(matrix, n , j):
    for i in range(n):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def zero_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                markRow(matrix, m , i)
                markCol(matrix, n , j)
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    

if __name__ == "__main__":
    matrix = [[1, 1, 1], 
              [1, 0, 1], 
              [1, 1, 1]]
    zero_matrix(matrix)
    for r in matrix:
        print(r, " \n ")