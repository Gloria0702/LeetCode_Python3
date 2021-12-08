def takeSecond(elem):
    return elem[1]
def eraseOverlapIntervals(intervals):
        num = 0
        intervals.sort(key=takeSecond)
        i = 0
        while i < len(intervals)-1:
             if intervals[i+1][0]<intervals[i][1]:
                num += 1
                del intervals[i+1]
             else: i += 1
        return num
print(eraseOverlapIntervals([[1,2], [2,4], [1,3]]))
print(eraseOverlapIntervals([[1,2], [1,2], [1,2]]))