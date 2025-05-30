from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        min_price, max_profit = prices[0], 0
        for price in prices[1:]:
            if price > min_price:
                max_profit = max(max_profit, price - min_price)
            else:
                min_price = price
        return max_profit


sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))