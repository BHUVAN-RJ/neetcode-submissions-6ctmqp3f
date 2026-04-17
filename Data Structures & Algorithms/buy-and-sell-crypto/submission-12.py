class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        profit = 0
        while r < len(prices):
            cur = prices[r] - prices[l]
            if cur < 0:
                 l = r
                 continue
            profit = max(cur, profit)
            r += 1
        return profit
        