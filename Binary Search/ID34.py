# def searchRange(nums, target):
#         l = len(nums)
#         if target not in nums:
#             return [-1,-1]
#         if l ==1:
#             return [0, 0]
#         i = int(l/2)
#         while i >= 0 and i <l:
#             if nums[i] > target:
#                 i = int(i/2)
#             elif nums[i]< target:
#                 i = int(l-i/2)
#             else:
#                 break
#         a=i
#         b=i
#         if i < l-1:
#             while nums[b] == target:
#                 b+=1
#         else:b+=1
#         while nums[a] == target:
#             a-=1
#         return [a+1,b-1]


# def searchRange(nums, target):
#         l = len(nums)
#         if target not in nums:
#             return [-1, -1]
#         a = nums.index(target)
#         b = a
#         if b < l - 1:
#             while nums[b] == target:
#                 b += 1
#         else:
#             b += 1
#         return [a, b - 1]
#
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        list_length = len(nums)
        if (list_length == 0) or (list_length == 1 and nums[0] != target):
            return [-1,-1]
        if (list_length == 1):
            return [0,0]
        midpoint = list_length//2
        print(nums[midpoint])
        if(nums[midpoint] > target):
            return self.searchRange(nums[:midpoint],target)
        if(nums[midpoint] < target):
            final_list = self.searchRange(nums[midpoint:],target)
            if final_list != [-1,-1]:
                return [x + midpoint for x in final_list]
            return final_list
        start = end = midpoint
        while nums[start] == target and start >= 0:
            start-=1
        start+=1
        while nums[end] == target:
            if (end == list_length-1):
                end = end+1 if nums[end] == target else end
                break
            end+=1
        end-=1
        return [start,end]

# print(searchRange([5,7,7,8,8,10],8))