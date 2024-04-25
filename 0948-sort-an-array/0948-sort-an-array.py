from random import randint

class Solution:

    def merge(self, listA, listB):
        sorted_nums = []

        i, j = 0, 0

        while i < len(listA) and j < len(listB):
            if listA[i] < listB[j]:
                sorted_nums.append(listA[i])
                i += 1
            else:
                sorted_nums.append(listB[j])
                j += 1
        
        return sorted_nums + listA[i:] + listB[j:]

    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left_half, right_half = nums[:mid], nums[mid:]

        sorted_left, sorted_right = self.mergeSort(left_half), self.mergeSort(right_half)

        sorted_nums = self.merge(sorted_left, sorted_right)

        return sorted_nums


    def sortArray(self, nums: List[int]) -> List[int]:

        return self.mergeSort(nums)

        



        