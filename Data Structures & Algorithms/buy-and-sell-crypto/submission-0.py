class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        profit = 0

        for price in prices[1:]:
            profit = max(price - curr_min, profit)
            curr_min = min(curr_min, price)
        
        return profit

        