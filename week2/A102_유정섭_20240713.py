# https://leetcode.com/problems/transpose-matrix/description/


class Solution:
    def transpose(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        ans = [[0] * n for _ in range(m)]
        # return ans
        for i in range(n):
            for j in range(m):
                ans[j][i] = matrix[i][j]
        return ans


print(Solution().transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().transpose([[1, 2, 3], [4, 5, 6]]))
print(Solution().transpose([[1, 4], [2, 5], [3, 6]]))
