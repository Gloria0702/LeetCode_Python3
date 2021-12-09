def take2(elem):
    return elem[1]
def findMinArrowShots(points):
        num = 0
        points.sort(key = take2)
        i =0
        ind = 1
        l = len(points)
        ida = l
        while (i <= l-1) and (ind+i <= l-1):
            ida -= 1
            while points[i][1] >= points[ind+i][0]:
                ind += 1
                ida -= 1
                if ind+i > l-1:
                    break
            num += 1
            i = i + ind
            ind = 1
        if (ida == 1):
            num += 1
        return num

print(findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))#2
print(findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))#4
print(findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))#2
print(findMinArrowShots([[1,9],[7,16],[2,5],[7,12],[9,11],[2,10],[9,16],[3,9],[1,3]]))#2
print(findMinArrowShots([[1,2]]))#1
print(findMinArrowShots([[-1,1],[0,1],[2,3],[1,2]]))#2