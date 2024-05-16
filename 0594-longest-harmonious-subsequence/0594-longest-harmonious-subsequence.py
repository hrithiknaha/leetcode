class Solution:
    def findLHS(self, nums: List[int]) -> int:

        # res = 0
        # for i in range(0, len(nums)):
        #     j = i + 1

        #     count = 0
        #     while j < len(nums):
        #         if abs(nums[j] - nums[i]) == 1:
        #             count += 1
        #         j += 1
        #     res = max(res, count)

        # return res

        occurence = {}

        for num in nums:
            if num not in occurence:
                occurence[num] = 1
            else:
                occurence[num] += 1
        
        res = 0
        for k, v in occurence.items():
            count = 0
            if k + 1 in occurence.keys():
                count = occurence[k] + occurence[k + 1]
            res = max(res, count)
        
        return res

            