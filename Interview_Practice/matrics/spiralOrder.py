# class Solution(object):
#     def spiralOrder(self, matrix):
#         top, bottom = 0, len(matrix) -1
#         left , right = 0, len(matrix[0]) -1
#         result = []
#         while top <= bottom and left <= right:
#             for i in range(left,right+1):
#                 result.append(matrix[top][i])
#             top += 1
#             for i in range(top, bottom+1):
#                 result.append(matrix[i][right])
#             right -= 1

#             if left <= right:
#                 for i in range(right, left -1, -1):
#                     result.append(matrix[bottom][i])
#                 bottom -= 1
    
#             if top <= bottom:
#                 for i in range(bottom, top-1, -1):
#                     result.append(matrix[i][left])
#                 left += 1
    
#         return result

class Solution(object):
    def spiralOrder(self, matrix):
        top, bottom = 0, len(matrix) -1
        left , right = 0, len(matrix[0]) -1
        result = []
        while top <= bottom and left <= right:
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left -1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1  # ✅ moved inside

            if left <= right:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1  # ✅ moved inside

        return result
    
    

if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] # Output: [1,2,3,4,8,12,11,10,9,5,6,7]
    obj = Solution()
    print(obj.spiralOrder(matrix))