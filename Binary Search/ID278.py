class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        value = dict()
        for i, elem in enumerate(nums):
            comp = target - elem
            if comp == 0 :
                return i
            elif comp < 0:
                return i
            value[elem] = i
        return i+1
