class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1 or x == 2: 
            return 1 

        for number in range(1, x):
            if number*number == x:
                return number
            else:
                if number*number > x and (number-1)*(number-1) < x:
                    return number-1

