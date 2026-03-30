class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = 0
        max_profit = 0
        while r < len(prices):#5
            print(prices[l], prices[r])
            cur_profit = prices[r] - prices[l] # 1 - 1 = 0
            if cur_profit <= 0: #l = 5
                l = r
            max_profit = max(cur_profit, max_profit) # max = 6
            r += 1
        return max_profit
            
