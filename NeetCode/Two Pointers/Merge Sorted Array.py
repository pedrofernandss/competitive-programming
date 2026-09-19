class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_pointer = len(nums1)-1

        while n > 0:
            nums1[nums1_pointer] = nums2[n-1]
            nums1_pointer -= 1
            n -= 1

        nums1.sort()