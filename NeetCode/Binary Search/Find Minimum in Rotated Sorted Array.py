class Solution:
    def is_before(self, nums, idx):
        return idx > 0 and nums[idx] < nums[idx-1]

    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        if len(nums) == 1:
            return nums[0]

        if nums[0] < nums[-1]:
            return nums[0]

        while l < r:
            middle = (l+r)//2

            if self.is_before(nums, middle):
                return nums[middle]
            
            if nums[middle] >= nums[0]:
                l = middle+1
            else:
                r = middle
        
        return nums[l]