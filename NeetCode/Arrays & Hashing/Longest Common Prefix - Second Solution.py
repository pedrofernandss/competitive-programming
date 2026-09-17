class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        prefix = strs[0]

        for idx_str in range(1, len(strs)):
            curr_str = strs[idx_str]
            idx_letter = 0
            while idx_letter < min(len(prefix), len(curr_str)):
                if prefix[idx_letter] != curr_str[idx_letter]:
                    break
                else:
                    idx_letter += 1                           
            prefix = prefix[:idx_letter]        
        
        return prefix