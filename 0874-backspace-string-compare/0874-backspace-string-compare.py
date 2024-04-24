class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        stack1 = []
        stack2 = []

        for char in s:
            if char == "#" and stack1:
                stack1.pop()
            elif char.isalpha():
                stack1.append(char)
        
        for char in t:
            if char == "#" and stack2:
                stack2.pop()
            elif char.isalpha():
                stack2.append(char)

        return stack1 == stack2
