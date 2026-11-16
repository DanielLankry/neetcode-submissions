class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L,R = 0,0
        maxProfit = 0

        for R in range(len(prices)):
            if prices[L] > prices[R]:
                L = R
            else:
                maxProfit = max(maxProfit, (prices[R] - prices[L]))

        return maxProfit


            
        