def Swap(array: list[str]):
    if len(array) < 3:
        return array
    
    prefix_len = len(array)//3
    sufix_len = (2*len(array))//3

    prefix = array[:prefix_len]
    sufix = array[prefix_len:sufix_len]

    ans = sufix+prefix

    return ans