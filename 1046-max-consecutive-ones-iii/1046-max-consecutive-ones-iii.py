class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = max_len = zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            if zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1 

            max_len = max(max_len, right - left + 1)
        return max_len