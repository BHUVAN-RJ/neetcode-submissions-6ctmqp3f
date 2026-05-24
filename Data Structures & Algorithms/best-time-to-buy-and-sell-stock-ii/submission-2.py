class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 1
        while i < len(prices):
            if prices[i] - prices[i-1] > 0:
                profit += prices[i] - prices[i-1]
            i += 1
        return profit

        