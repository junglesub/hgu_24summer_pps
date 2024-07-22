# https://leetcode.com/problems/move-zeroes/


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroCount = nums.count(0)
        newNums = [num for num in nums if num != 0] + ([0] * zeroCount)

        for i in range(len(nums)):
            nums[i] = newNums[i]


test = [0, 1, 0, 3, 12]
Solution().moveZeroes(test)
print(test)
