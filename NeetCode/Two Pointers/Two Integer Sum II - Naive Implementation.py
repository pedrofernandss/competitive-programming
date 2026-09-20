class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for first_pointer in range(len(numbers)):
            for second_pointer in range(first_pointer+1, len(numbers)):
                if numbers[first_pointer] + numbers[second_pointer] == target:
                    return [first_pointer+1, second_pointer+1]
