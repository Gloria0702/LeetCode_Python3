import math


def judgeSquareSum(c):
        if c >= 0:
            max = int(math.sqrt(c))
            l = 0
            r = max
            result = False
            while (r>=l):
                if (l**2+r**2) == c:
                    result = True
                    break
                elif (l**2+r**2) < c:
                    l+=1
                else:
                    r-=1
        else: result = False
        return result
judgeSquareSum(1)