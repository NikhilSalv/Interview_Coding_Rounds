class Solution(object):
    def trap(self, height):
        stack = []
        water = 0
        n = len(height)
        
        for i in range(n):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                
                if not stack:
                    break  # no left boundary
                
                distance = i - stack[-1] - 1
                bounded_height = min(height[i], height[stack[-1]]) - height[top]
                
                water += distance * bounded_height
            
            stack.append(i)
        
        return water

if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    solution = Solution()
    print(solution.trap(height))  # Output: 6