class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x
        l = 1
        r = x
        while (l<=r):
            mid = int(l+(r-l)/2)
            sqrt = int(x/mid)
            if sqrt == mid:
                return mid
            elif mid>sqrt:
                r = mid-1
            else:
                l = mid+1
        return r


#CASE2
    def mySqrt1(self, x: int) -> int:
        a = x
        while a*a> x:
            a = int((a+x/a)/2)

        return x