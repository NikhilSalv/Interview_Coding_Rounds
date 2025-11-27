class Solution:
    def largestRectangleArea(self, heights):
        stack =[]
        max_area = 0
        heights.append(0)  # Append a sentinel value to pop all remaining bars

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] -1
                max_area = max(max_area, height * width)
            
            stack.append(i)

        return max_area



if __name__ == "__main__": 
    heights = [2,1,5,6,2,3]
    solution = Solution()
    print(solution.largestRectangleArea(heights))  # Output: 10