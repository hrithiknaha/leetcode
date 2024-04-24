class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start_index = 0
        max_count = 0
        char = dict()

        for i in range(len(s)):
            if s[i] in char:
                start_index = max(start_index, char[s[i]] + 1)
            char[s[i]] = i
            max_count = max(max_count, i + 1 - start_index) 

        return max_count   
