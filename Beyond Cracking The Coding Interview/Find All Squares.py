def findAllSquares(array: List[int]) -> List[List[int]]:
    hashmap = {}
    ans = []

    for idx in range(len(array)):
        value = array[idx]
        hashmap[value] = idx

    for key in hashmap:
        square = (key*key)
        
        if square in hashmap:
            ans.append([hashmap[key], hashmap[square]])
    
    return ans