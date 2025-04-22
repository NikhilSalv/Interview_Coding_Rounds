
def notOverlapping(activities):
    result = []

    activities.sort(key=lambda x: x[1])
    print("sorted :", activities)
    current_endTime = activities[0][1]
    n = len(activities)
    result = []
    result.append(activities[0])

    for i in range(1, n):
        if activities[i][0] >= current_endTime:
            result.append(activities[i])
            current_endTime = activities[i][1]
    return result



if __name__ == "__main__":
    activities = [(5, 7), (8, 9),(1, 4), (4, 5), (4, 6)] # [(1, 4), (4, 5), (5, 7), (8, 9)]
    print(notOverlapping(activities))
    
    
    
