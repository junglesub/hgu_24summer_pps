# https://leetcode.com/problems/single-number/description/


class Solution:
    def singleNumber(self, nums) -> int:
        return min(nums, key=lambda x: nums.count(x))


print(Solution().singleNumber([2, 2, 1]))
