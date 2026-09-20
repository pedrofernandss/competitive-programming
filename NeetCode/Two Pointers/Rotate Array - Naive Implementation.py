class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for time in range(1, k+1):
            left_pointer = 0
            right_pointer = 1
            first_num = nums[0] 

            while right_pointer < len(nums):
                temp_num = nums[right_pointer]
                nums[right_pointer] = nums[left_pointer]
                nums[left_pointer] = temp_num
                right_pointer += 1
                left_pointer += 1
