class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()

        for idx_number1 in range(len(nums)):
            for idx_number2 in range(idx_number1+1, len(nums)):
                for idx_number3 in range(idx_number2+1, len(nums)):
                    if nums[idx_number1] + nums[idx_number2] + nums[idx_number3] == 0:
                        triplet = (nums[idx_number1], nums[idx_number2], nums[idx_number3])
                        ans.add(triplet)
                        
        
        return [list(x) for x in ans]