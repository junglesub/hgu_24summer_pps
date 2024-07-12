# https://leetcode.com/problems/min-stack/


class MinStack:

    def __init__(self):
        self.arr = []
        self.minArr = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if len(self.minArr) == 0:
            self.minArr = [val]
        else:
            self.minArr.append(min(self.minArr[-1], val))
        return

    def pop(self) -> None:
        self.arr.pop()
        self.minArr.pop()
        return

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minArr[-1]
