class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        maxSum = 0
        
        for i in range(k):
            maxSum = maxSum + cardPoints[i]

        currSum = maxSum
        for j in range(k):
            currSum = currSum - cardPoints[k - 1 - j] + cardPoints[len(cardPoints) - 1 - j]

            maxSum = max(currSum, maxSum)
        
        return maxSum




        



        