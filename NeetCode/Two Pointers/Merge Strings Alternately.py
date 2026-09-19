class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer_word1 = 0
        pointer_word2 = 0
        final_word = ""

        while pointer_word1 <= len(word1)-1 and pointer_word2 <= len(word2)-1:
                final_word += word1[pointer_word1]
                pointer_word1 += 1
            
                final_word += word2[pointer_word2]
                pointer_word2 += 1
                
        if pointer_word1 > len(word1)-1:
            final_word += word2[pointer_word2:]

        if pointer_word2 > len(word2)-1:
            final_word += word1[pointer_word1:]
                    
        return final_word
