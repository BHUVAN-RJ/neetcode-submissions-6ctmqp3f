class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = r = 0
        for i in range(len(prices)):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
            r += 1
            res = max(profit, res)
        return res

        