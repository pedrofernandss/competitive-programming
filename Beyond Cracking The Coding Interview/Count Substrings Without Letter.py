def countSubstrings(string):
    if len(string) == 0:
        return 0
    
    totalSubstrings = 0
    currentSubstringsInWindonw = 0

    for idx in range(len(string)):
        if string[idx] == 'a':
            currentSubstringsInWindonw = 0
        else:
            currentSubstringsInWindonw += 1
            totalSubstrings += currentSubstringsInWindonw 

    return totalSubstrings 