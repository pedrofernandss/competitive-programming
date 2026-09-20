class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and target == nums[0]:
            return 0
        idx = 0
        while idx <= len(nums)-1:
            if nums[idx] == target:
                return idx
            idx += 1
        return -1 