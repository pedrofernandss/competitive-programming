class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx in range(len(numbers)):
            number_to_find = target - numbers[idx]

            left_pointer = idx+1
            right_pointer = len(numbers)-1

            while left_pointer <= right_pointer:
                middle = (right_pointer+left_pointer)//2

                if number_to_find == numbers[middle]:
                    return [idx+1, middle+1]
                elif number_to_find < numbers[middle]:
                    right_pointer = middle - 1
                else:
                    left_pointer = middle + 1