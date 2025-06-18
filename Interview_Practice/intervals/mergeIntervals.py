class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        
        intervals.sort(key = lambda x : x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        n = len(intervals)
        result = []
        for i in range(1,n):
            current_start , current_end = intervals[i]
            if current_start < end:
                end = max(end, current_end)
            else:
                result.append([start, end])
                start = current_start
                end = current_end
        result.append([start, end])
        return result
    

if __name__ == "__main__":
    intervals = [[5,10],[1,3],[9,18],[2,6]]
    obj = Solution()
    print(obj.merge(intervals))

    intervals.sort(key = lambda x : x[0])
    print("sorted : ", intervals)
    print("sorted end time : ", intervals[1])