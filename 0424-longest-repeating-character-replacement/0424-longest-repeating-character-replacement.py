class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = max_len = 0

        char_freq = {}

        for right in range(len(s)):

            if s[right] in char_freq:
                char_freq[s[right]] += 1
            else:
                char_freq[s[right]] = 1

            max_freq = max(char_freq.values())

            while ((right - left + 1) - max_freq > k):
                char_freq[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len





        