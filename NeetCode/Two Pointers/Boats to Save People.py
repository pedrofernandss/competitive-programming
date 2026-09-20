class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        boats = 0
        left_pointer = 0
        right_pointer = len(people)-1

        while left_pointer <= right_pointer:
            if people[left_pointer] + people[right_pointer] <= limit:
                boats += 1
                right_pointer -= 1
                left_pointer += 1
            elif people[left_pointer] + people[right_pointer] > limit:
                right_pointer -= 1
                boats += 1
        
        return boats