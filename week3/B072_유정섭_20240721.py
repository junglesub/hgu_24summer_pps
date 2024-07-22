# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

from itertools import combinations


class Solution:
    def maxProfit(self, prices) -> int:
        buy = prices[0]
        profit = 0
        for p in prices:
            buy = min(buy, p)
            profit = max(profit, p - buy)
        return profit
        # return max(0, prices[(m := max(combinations(range(len(prices)), 2), key=lambda x: prices[x[1]] - prices[x[0]]))[1]] - prices[m[0]]) if len(prices) > 1 else 0


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
