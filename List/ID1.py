class Solution:
    def twoSum(self, nums: List[int], target: int):
        value = dict()
        for i, elem in enumerate(nums):
            comp = target - elem
            if comp in value:
                return [value[comp],i]
            value[elem] = i
        return []