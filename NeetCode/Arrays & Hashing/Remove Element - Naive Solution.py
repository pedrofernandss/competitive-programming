class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temporary_array = []

        for number in nums:
            if number == val:
                continue
            else:
                temporary_array.append(number)
        
        for idx in range(len(temporary_array)):
            nums[idx] = temporary_array[idx]
        
        return len(temporary_array)