class Solution:
    def mySqrt(self, x: int) -> int:
        left_pointer, right_pointer = 0, x
        nearest_value = 0

        while  left_pointer <= right_pointer:
            middle_value = (right_pointer+left_pointer)//2

            if middle_value*middle_value == x:
                return middle_value
            elif middle_value*middle_value > x:
                right_pointer = middle_value-1
            else:
                left_pointer = middle_value+1
                nearest_value = middle_value

        return nearest_value