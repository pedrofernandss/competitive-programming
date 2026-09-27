def findTriplets(arr, w):
    if len(arr) < 3:
        return False
    
    arr = sorted(arr)

    for idx in range(len(arr)):
        left_pointer = idx+1
        right_pointer = len(arr)-1

        while left_pointer < right_pointer:
            value = arr[idx] + arr[left_pointer] + arr[right_pointer]   
            if value == w:
                return True
            elif value > w:
                right_pointer -= 1
            else:
                left_pointer += 1
    
    return False
        