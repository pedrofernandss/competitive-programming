class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        for sp in range(len(nums)):
            for fp in range(sp+1, len(nums)):
                if nums[sp] == nums[fp] and abs(sp-fp) <= k:
                    return True
        return False