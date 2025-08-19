class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key=lambda x:x[0])
        end = points[0][1]
        arrow = 1
        for i in range(1,len(points)):
            current_s, current_e = points[i]
            if current_s > end:
                arrow += 1
                end = current_e
        return arrow

            
        return len(merged_points)

if __name__ == "__main__":
    points = [[10,16],[2,8],[1,6],[7,12],[13,20]] # [[1,6],[2,8],[7,12],[10,16]] >> [1,12],[10,16] 
    obj = Solution()
    print(obj.findMinArrowShots(points))