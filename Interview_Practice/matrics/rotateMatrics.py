class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)

    # Step 1: Transpose
        for i in range(n):
            for j in range(i + 1, n):  # j > i to avoid re-swapping
                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()
        return matrix
        

if __name__ == "__main__":
    matrix = [[1,2,3,10],
              [4,5,6,11],
              [7,8,9,12],
              [22,34,27,86]]
    obj = Solution()
    print(obj.rotate(matrix))

