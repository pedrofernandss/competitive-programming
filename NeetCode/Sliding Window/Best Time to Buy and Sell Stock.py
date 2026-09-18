class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day = 0
        sell_day = 1
        profit = 0

        for buy_day in range(len(prices)):
            for sell_day in range(buy_day+1, len(prices)):
                profit = max(profit, (prices[sell_day]-prices[buy_day]))

        if profit < 0:
            return 0
        return profit