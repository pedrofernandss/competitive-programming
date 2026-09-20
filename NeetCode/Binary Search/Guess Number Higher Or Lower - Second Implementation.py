class Solution:
    def guessNumber(self, n: int) -> int:
        left_pointer = 1
        right_pointer = n

        while left_pointer <= right_pointer:
            middle = (right_pointer+left_pointer)//2
            response = guess(middle)
            
            if response == 0:
                return middle
            elif response == -1:
                right_pointer = middle - 1
            else:
                left_pointer = middle + 1 