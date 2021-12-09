class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        test = set(nums)
        a = len(test)
        b = len(nums)
        if b-a == 0:
            return False
        else:
            return True

