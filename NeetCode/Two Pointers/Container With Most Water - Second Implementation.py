class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = 0
        left_pointer = 0
        right_pointer = len(heights)-1

        while left_pointer < right_pointer:
            width = right_pointer - left_pointer
            height = min(heights[left_pointer], heights[right_pointer])
            
            amount = width*height
            max_amount = max(max_amount, amount)

            #Movo o ponteiro da menor altura, procurando uma maior por que se mover o da maior, vou estar encurtando a distância e mantendo a mesma altura 
            if heights[left_pointer] < heights[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_amount