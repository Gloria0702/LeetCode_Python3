class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        insertPos = m + n - 1  # Length of merged array
        m, n = m - 1, n - 1  # Last index of both the array

        while m >= 0 and n >= 0:
            # As the list is sorted, compare from last and and put the grater element at insertpos

            if nums1[m] > nums2[n]:
                nums1[insertPos] = nums1[m]
                m -= 1  # Move the pointer to next larger
            else:
                nums1[insertPos] = nums2[n]
                n -= 1  # Move the pointer to next larger
            insertPos -= 1

            # if nums two has any smaller elements than nums1 left , this final while loop will add it to nums1
        while n >= 0:
            nums1[insertPos] = nums2[n]
            n -= 1
            insertPos -= 1
