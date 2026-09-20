class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = 0

        for left_pointer in range(len(heights)):
            for right_pointer in range(left_pointer+1, len(heights)):
                width = right_pointer - left_pointer
                height = min(heights[left_pointer], heights[right_pointer])
                amount = width*height
                max_amount = max(max_amount, amount)
        
        return max_amount