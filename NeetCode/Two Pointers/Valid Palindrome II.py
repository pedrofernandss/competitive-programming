class Solution:
    def isAlphanumeric(self, char: str) -> bool:
        return (ord(char) >= ord('0') and ord(char) <= ord('9')) or (ord(char) >= ord('a') and ord(char) <= ord('z'))

    def isPalindrome(self, s: str) -> bool:
        left_pointer, right_pointer = 0, len(s)-1

        while(left_pointer <= right_pointer):
            if not self.isAlphanumeric(s[left_pointer]):
                left_pointer += 1
            elif not self.isAlphanumeric(s[right_pointer]):
                right_pointer -= 1
            else:
                if s[left_pointer] != s[right_pointer]:
                    return False
                
                left_pointer += 1
                right_pointer -= 1
        
        return True

    def validPalindrome(self, s: str) -> bool:
        left_pointer = 0
        right_pointer = len(s)-1

        if self.isPalindrome(s):
            return True

        while (left_pointer <= right_pointer):
            if s[left_pointer] == s[right_pointer]:
                left_pointer += 1
                right_pointer -= 1
            else:
                strinWithoutLeft = s[:left_pointer] + s[left_pointer+1:]
                stringWithouRight = s[:right_pointer] + s[right_pointer+1:]
                return self.isPalindrome(strinWithoutLeft) or self.isPalindrome(stringWithouRight)
        return False
