class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        max_size = 0
        seen = set()

        while right < len(s):
            can_grow = s[right] not in seen
            if can_grow:
                seen.add(s[right])
                max_size = max(max_size, right-left+1)
                right += 1
            else:
                seen.remove(s[left])
                left +=1
                
        return max_size
