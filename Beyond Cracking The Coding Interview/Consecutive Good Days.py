def consecutiveGoodDays(projected_sales: list[int], k: int)-> int:
    left_pointer = 0
    right_pointer = 0
    boostedGiven = 0
    maxConsecutiveDays = 0

    while left_pointer <= len(projected_sales)-1 and right_pointer <= len(projected_sales)-1:
        if projected_sales[right_pointer] >= 5:
            if projected_sales[right_pointer] < 10 and boostedGiven < k:
                right_pointer += 1
                boostedGiven += 1
            elif projected_sales[right_pointer] >= 10:
                right_pointer += 1
            else:
                maxConsecutiveDays = max(maxConsecutiveDays, (right_pointer-left_pointer))
                if projected_sales[left_pointer] >= 5 and projected_sales[left_pointer] < 10:
                    boostedGiven -= 1
                left_pointer += 1
        else:
            right_pointer += 1
            left_pointer = right_pointer
            boostedGiven = 0
    
    maxConsecutiveDays = max(maxConsecutiveDays, (right_pointer-left_pointer))
    
    return maxConsecutiveDays
