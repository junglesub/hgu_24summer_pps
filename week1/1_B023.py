# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/


class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.nums = nums
        self.maxK = list(sorted(self.nums)[-self.k :])

    def add(self, val: int) -> int:
        self.maxK.append(val)
        self.maxK = list(sorted(self.maxK)[-self.k :])
        return self.maxK[0]
