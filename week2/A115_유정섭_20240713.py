# https://leetcode.com/problems/maximum-number-of-balloons/


class Solution:
    def maxNumberOfBalloons(self, text):
        return int(min(text.count("b"), text.count("a"), text.count("l") / 2, text.count("o") / 2, text.count("n")))


print(Solution().maxNumberOfBalloons("nlaebolko"))
print(Solution().maxNumberOfBalloons("loonbalxballpoon"))
print(Solution().maxNumberOfBalloons("leetcode"))
