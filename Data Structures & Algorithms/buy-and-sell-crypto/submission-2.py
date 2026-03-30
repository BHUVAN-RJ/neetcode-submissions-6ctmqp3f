class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        l = 0
        r = 1
        profit = 0
        while r < len(prices):
            print(prices[r])
            curP = prices[r] - prices[l]
            if curP <= 0:
                l = r
                r += 1
                continue
            profit = max(profit, curP)
            r += 1
        return profit


        