class Solution:
    def reverseVowels(self, s: str) -> str:

        list_value = list(s)

        check = "aeiouAEIOU"

        low, high = 0, len(s) - 1

        while low <= high:
            while low < high and s[low] not in check:
                low += 1
            while high > low and s[high] not in check:
                high -= 1
            
            list_value[low], list_value[high] = list_value[high], list_value[low]

            low += 1
            high -= 1

        return "".join(list_value)