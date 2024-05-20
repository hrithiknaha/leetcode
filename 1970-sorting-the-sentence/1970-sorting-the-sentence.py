class Solution:
    def sortSentence(self, s: str) -> str:

        words = s.split()
        sorted_words = [None] * len(words)
        res = ""
        count = 1

        for word in words:
            sorted_words[int(word[-1]) - 1] = word[:-1]
        
        for word in sorted_words:
            res += word
            if count < len(words):
                res += " "
                count += 1
        
        return res
        