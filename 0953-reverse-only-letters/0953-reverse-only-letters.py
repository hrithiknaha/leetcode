class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        str_list = list(s)

        low, high = 0, len(s) - 1

        while low < high:
            while low < high and not str_list[low].isalpha():
                low += 1
            while high > low and not str_list[high].isalpha():
                high -= 1
            
            str_list[low], str_list[high] = str_list[high], str_list[low]

            low += 1
            high -= 1
        
        return "".join(str_list)