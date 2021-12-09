class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum_of_nums = sum(nums)
        sum_set_of_nums = sum(set(nums)) * 2
        return sum_set_of_nums - sum_of_nums