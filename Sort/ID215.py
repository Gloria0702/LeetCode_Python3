class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort() #Sort list from smallest to biggest number
        return nums[-k] #Return the "k"th biggest item by indexing in reverse