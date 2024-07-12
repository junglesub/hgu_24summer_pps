# https://leetcode.com/problems/count-and-say/


class Solution:
    def countAndSay(self, n):
        s = "1"
        for i in range(1, n):
            s = self.rle(s)
        return s

    def rle(self, s):
        arr = []
        for c in s:
            if not arr or arr[-1][0] is not c:
                arr.append(c)
            else:
                arr[-1] += c
        return "".join(map(lambda x: f"{len(x)}{x[0]}", arr))


print(Solution().countAndSay(1))
print(Solution().countAndSay(2))
print(Solution().countAndSay(3))
print(Solution().countAndSay(4))
