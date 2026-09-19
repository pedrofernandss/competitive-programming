class Solution:
    def isAlphanumeric(self, char: str) -> bool:
        if (ord(char) >= 48 and ord(char) <= 57) or (ord(char) >= 97 and ord(char) <= 122):   
            return True
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left_pointer = 0
        right_pointer = len(s)-1

        while(left_pointer <= right_pointer):
            if not self.isAlphanumeric(s[left_pointer]):
                left_pointer += 1
                continue

            if not self.isAlphanumeric(s[right_pointer]):
                right_pointer -= 1
                continue
            
            if s[left_pointer] != s[right_pointer]:
                return False
            
            left_pointer += 1
            right_pointer -= 1
        
        return True