class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 pass -> 1st pass I get the place where we need to buy if any
        # second pass we get the place to sell
        if len(prices) < 2:
            return 0
        l, r = 0, 0
        profit = 0
        while r + 1 < len(prices):
            r += 1
            if prices[r] <= prices[l]:
                l = r
                continue
            diff = prices[r] - prices[l]
            profit = max(profit, diff)        
        return profit