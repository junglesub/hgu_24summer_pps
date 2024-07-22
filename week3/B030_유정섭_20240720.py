# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/


class Solution:
    def largestSumAfterKNegations(self, nums, k):
        for _ in range(k):
            nums[nums.index(min(nums))] *= -1
        return sum(nums)


print(Solution().largestSumAfterKNegations([4, 2, 3], 1))
print(Solution().largestSumAfterKNegations([3, -1, 0, 2], 3))
