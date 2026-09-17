class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)

        if len(nums) == 1:
            return False
        else:
            for idx in range(len(nums)):
                if nums[idx] == nums[idx-1]:
                    return True
            return False