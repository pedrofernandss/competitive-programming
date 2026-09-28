def OptimizedSolution(array: list[str]):
    if len(array) < 3:
        return array
    
    first_pointer = 0
    second_pointer = len(array)//3 
    thrid_pointer = (2*len(array))//3

    while first_pointer < len(array)//3:
        array[first_pointer], array[second_pointer], array[thrid_pointer] = array[second_pointer], array[thrid_pointer], array[first_pointer]

        first_pointer += 1
        second_pointer += 1
        thrid_pointer += 1

    return array 
