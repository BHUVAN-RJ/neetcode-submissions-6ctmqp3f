class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        profit = 0
        while r < len(prices):
            if prices[r] <= prices[l]:
                l = r
                r += 1
            else:
                cur = prices[r] - prices[l]
                profit = max(cur, profit)
                r += 1
        return profit

