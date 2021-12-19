def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    #method1
    # if n > 0:
    #     if m > 0:
    #         nums1 = nums1[:m]
    #         for i in range(n):
    #             nums1.append(nums2[i])
    #         nums1.sort()
    #     else:
    #         nums1 = nums2.sort()
    # else:
    #     nums1.sort()
    # return nums1

    #method2
    # arr = []
    # for i in range(m):
    #     arr.append(nums1[i])
    # for j in range(n):
    #     arr.append(nums2[j])
    # arr.sort()
    # nums1[:] = arr[:m + n]

    #method3
    pos = m + n - 1
    while m-1 >= 0 and n-1 >= 0:
        if (nums1[m - 1] > nums2[n - 1]):
            nums1[pos] = nums1[m - 1]
            m -= 1
        else:
            nums1[pos] = nums2[n - 1]
            n -= 1

        pos -= 1
    while n-1 >= 0:
        nums1[pos] = nums2[n - 1]
        pos -= 1
        n -= 1
print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))