def searchInGrid(grid: List[List[int]], target: int) -> List[int]:
    answer = []
    rows = len(grid)
    columns = len(grid[0])

    left_pointer_idx = 0
    right_pointer_idx = (rows*columns)-1

    #for idx in range((rows*columns)-1):
    while (left_pointer_idx <= right_pointer_idx):
        middle_idx = (left_pointer_idx+right_pointer_idx)//2

        middle_row_idx = middle_idx//columns
        middle_column_idx = middle_idx%columns

        if grid[middle_row_idx][middle_column_idx] == target:
            return [middle_row_idx, middle_column_idx]
        elif grid[middle_row_idx][middle_column_idx] > target:
            right_pointer_idx = middle_idx-1
        else:
            left_pointer_idx = middle_idx+1
    
    return [-1, -1]