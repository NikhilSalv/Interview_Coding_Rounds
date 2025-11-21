class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        output = [[0]* len(matrix) for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                output[j][i] = matrix[i][j]

        return output
        

if __name__ == "__main__":
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    obj = Solution()
    print(obj.transpose(matrix))  
    matrix2 = [[1,2,3,4],
               [5,6,7,8]] 
    print(obj.transpose(matrix2))  # Expected output [[1,5],[2,6],[3,7],[4,8]]