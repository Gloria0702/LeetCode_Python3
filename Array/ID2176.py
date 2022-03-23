class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        while nums:
            a = nums.pop()
            l = len(nums)
            for i,j in enumerate(nums):
                if (j == a) and (i*l%k ==0):
                    result += 1
                    # print("s",j,"id",i,"l",a,"id",l)
            l-=1
        return result
nums = [5,5,9,2,5,5,9,2,2,5,5,6,2,2,5,2,5,4,3]
k = 7
t1 = [3,1,2,2,2,1,3]
t1_1 = 2
t2 = [1,2,3,4]
t2_1 = 1
out = Solution()
s = out.countPairs(nums,k)
o1 = out.countPairs(t1,t1_1)
o2 = out.countPairs(t2,t2_1)