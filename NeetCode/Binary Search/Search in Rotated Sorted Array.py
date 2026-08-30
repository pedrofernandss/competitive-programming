class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while(left <= right):
            middle = (right + left)//2

            if nums[middle] == target:
                return middle

            # Vemos se a esquerda está ordenada
            if nums[left] <= nums[middle]:
                # Vemos se o target está contido no intervalo da esquerda (que está ordenado)
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1

            # Vemos se a direita está ordenada
            else:
                # Vemos se o target está contido no intervalo da direita (que está ordenado)
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1

        return -1