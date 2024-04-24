class Solution:
    def removeDuplicates(self, s: str) -> str:

        stack = []

        for char in s:
            if char not in stack or stack[-1] not in char:
                stack.append(char)
            else:
                stack.pop()

        return "".join(stack)
        