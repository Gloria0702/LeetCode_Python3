def topKFrequent(nums, k):
        a = set(nums)
        a = list(a)
        b = []
        c = []
        for i in a:
            b.append(nums.count(i))
        for i in range(k):
            d = b.index(max(b))
            c.append(a[d])
            del b[d]
            del a[d]
        return c
print(topKFrequent([1,1,1,2,2,3],2))
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return [x[0] for x in c.most_common()[:k]]