class Solution:
    def reverseString(self, s: List[str]) -> None:
        left_pointer = 0
        right_pointer = len(s)-1
        auxiliar = s[left_pointer]

        while(left_pointer < right_pointer):
            s[left_pointer] = s[right_pointer]
            s[right_pointer] = auxiliar
            
            left_pointer += 1
            right_pointer -= 1
            auxiliar = s[left_pointer]