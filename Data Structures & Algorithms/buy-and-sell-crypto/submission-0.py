class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        low = prices[0]
        for n in prices:
            prof = max(prof, n - low)  # best sell using the cheapest buy before now
            low = min(low, n)          # then update the cheapest buy
        return prof


        