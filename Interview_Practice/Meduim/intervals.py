def insert(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)

    # Step 1: Add all intervals before newInterval (no overlap)
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Step 2: Merge overlapping intervals with newInterval
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)

    # Step 3: Add remaining intervals after newInterval
    while i < n:
        result.append(intervals[i])
        i += 1

    return result


if __name__ == "__main__":
    intervals = [[1,2], [3,10], [4,8], [6,7], [8,10], [12,16]]
    newInterval = [3,10]
    intervals2 = [[1,3],[6,9]]
    newInterval2 = [2,5]
    intervals3 = [[1,3],[6,9]]
    newInterval3 = [2,5]
    print(insert(intervals3,newInterval3))