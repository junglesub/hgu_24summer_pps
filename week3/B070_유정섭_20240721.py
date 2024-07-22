# https://leetcode.com/problems/min-cost-climbing-stairs/


class Solution:
    def minCostClimbingStairs(self, cost):
        costTb = [0] * len(cost)
        costTb[0] = cost[0]
        costTb[1] = cost[1]
        for i in range(2, len(cost)):
            costTb[i] = cost[i] + min(costTb[i - 1], costTb[i - 2])
        return min(costTb[-1], costTb[-2])
