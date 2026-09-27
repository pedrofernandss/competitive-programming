def twoSum(arr):
    if len(arr) < 2:
        return False
    
    left_pointer = 0
    right_pointer = len(arr)-1

    while left_pointer < right_pointer:
        currentSum = arr[left_pointer] + arr[right_pointer]

        if currentSum == 0:
            return True
        elif currentSum > 0:
            right_pointer -= 1
        else:
            left_pointer += 1

    return False