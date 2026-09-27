class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        numsSorted = sorted(nums)

        left_pointer = 0
        right_pointer = len(numsSorted)-1

        while left_pointer <= right_pointer:
            idx_middle = (right_pointer+left_pointer)//2

            if numsSorted[idx_middle] == target:
                return True
            elif numsSorted[idx_middle] > target:
                right_pointer = idx_middle - 1
            else:
                left_pointer = idx_middle + 1
        
        print(f'final middle {idx_middle}')
        return False
