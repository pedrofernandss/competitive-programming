class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mostFrequent = {}

        for num in nums:
            if num not in mostFrequent:
                mostFrequent[num] = 1
            else:
                mostFrequent[num] += 1

        sortedMostFrequent = sorted(mostFrequent.keys(), key=lambda x: mostFrequent[x], reverse=True)
        
        return sortedMostFrequent[:k]