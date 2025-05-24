
def rotate(matrix):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j] = matrix[j][i]
    for row in matrix:
        row.reverse()

    
    return matrix



if __name__ == "__main__":
    matrix = [[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]]
    
    print(rotate(matrix)) # [[1,4,7], [2,5,8], [3,6,9]]

    # expected_op = 
    # [[7,4,1],
    # [8,5,2],
    # [9,6,3]]