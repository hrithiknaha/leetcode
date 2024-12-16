class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        def expand_from_middle(left, right):
            while (left >= 0 and right < n and s[left] == s[right]):
                left -= 1
                right += 1
            return s[left + 1: right]

        max_str = s[0]

        for i in range(len(s) - 1):
            odd = expand_from_middle(i, i)
            even = expand_from_middle(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even
        
        return max_str


