# https://leetcode.com/problems/n-th-tribonacci-number/


class Solution:
    def __init__(self) -> None:
        self.store = {}

    def tribonacci(self, n: int) -> int:
        if n in self.store.keys():
            return self.store[n]

        if n == 0:
            self.store[n] = 0
            return 0
        if 1 <= n <= 2:
            self.store[n] = 1
            return 1

        self.store[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        return self.store[n]
