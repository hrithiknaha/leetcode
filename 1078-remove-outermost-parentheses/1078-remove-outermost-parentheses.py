class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        result = ""
        count = 0

        j = 0

        for i in range(len(s)):
            if s[i] == "(":
                count += 1
            else:
                count -= 1

            if count == 0:
                result += s[j + 1: i]
                j =  i + 1
            
        return result
        