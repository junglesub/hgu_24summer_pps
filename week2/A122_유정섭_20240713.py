# https://leetcode.com/problems/rotate-string/


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(goal) >= len(s) and s in (goal * 2)


print(Solution().rotateString("abcde", "cdeab"))
print(Solution().rotateString("abcde", "abced"))
