class Solution:
    def totalFruit(self, fruits):
        
        left = max_len = 0

        fruit_count = dict()

        for right in range(len(fruits)):

            if fruits[right] in fruit_count:
                fruit_count[fruits[right]] += 1
            else:
                fruit_count[fruits[right]] = 1
            
            if len(fruit_count.keys()) > 2:
                if fruits[left] in fruit_count:
                    fruit_count[fruits[left]] -= 1
                    if fruit_count[fruits[left]] == 0:
                        del fruit_count[fruits[left]]
                    left += 1
            
            max_len=max(max_len, sum(fruit_count.values()))

        return max_len