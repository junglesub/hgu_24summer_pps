# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/


class Solution:
    def twoSum(self, numbers, target: int):
        d = dict(zip(numbers, range(len(numbers))))
        for n in numbers:
            if (need := target - n) in d.keys():
                if need == n and (numbers[d[need]] == numbers[d[need] - 1]):
                    return [d[need], d[need] + 1]
                return [d[n] + 1, d[need] + 1]


print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([2, 3, 3], 6))
print(Solution().twoSum([0, 0, 3, 4], 0))
