class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap_s = {}
        for i in range(len(s)):
            if s[i] not in hashmap_s:
                hashmap_s[s[i]] = 1
            else:
                hashmap_s[s[i]] += 1 

        hashmap_t = {}
        for i in range(len(t)):
            if t[i] not in hashmap_t:
                hashmap_t[t[i]] = 1
            else:
                hashmap_t[t[i]] += 1 

        if hashmap_s == hashmap_t:
            return True
        else:
            return False