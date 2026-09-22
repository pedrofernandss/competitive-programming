class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = []
        seen = set()
        n = len(grid[0])
        
        for row in grid:
            for value in row:
                if value not in seen:
                    seen.add(value)
                else:
                    ans.append(value)      
        
        expectedValues = [x for x in range(1, n*n)]
        seenSorted = sorted(seen)

        for idx in range(len(seenSorted)):
            if expectedValues[idx] != seenSorted[idx]:
                ans.append(expectedValues[idx])
                return ans
        
        ans.append(expectedValues[-1]+1)

        return ans