class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l, r = 0, 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
            r += 1
            res = max(profit, res)
        
        return res
            



        