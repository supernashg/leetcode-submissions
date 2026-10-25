class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        maps = {']': '[', ')': '(', '}': '{'}

        for char in s:
            if char in maps:
                if not stack or maps[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        return not stack

    

