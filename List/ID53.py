class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far=nums[0]
        max_till_now=nums[0]
        for i in range(1,len(nums)):
            max_till_now=max(nums[i],max_till_now+nums[i])
            max_so_far=max(max_so_far,max_till_now)
        return max_so_far
