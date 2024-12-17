class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_dict = dict()
        start_index = max_count = 0

        for right in range(len(s)):
            if s[right] in char_dict:
                start_index = max(start_index, char_dict[s[right]] + 1)
            char_dict[s[right]] = right
        
            max_count = max(max_count, right - start_index + 1)
    
        return max_count
        