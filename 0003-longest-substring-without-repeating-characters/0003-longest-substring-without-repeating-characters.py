class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        count = 0
        result = 0

        for i in range(len(s)): 
            dict_s = {}
            count = 0
            j = i 

            while  j < len(s):
                if s[j] not in dict_s:
                    count += 1
                    dict_s[s[j]] = 1
                    j += 1
                    result = max(count, result)
                else:
                    break
        
        return result       