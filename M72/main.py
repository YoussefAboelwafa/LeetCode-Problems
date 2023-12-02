class Solution(object):
    def minDistance(self, word1, word2):
        word1 = "0" + word1
        word2 = "0" + word2
        m = len(word2)
        n = len(word1)
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            dp[i][0] = i

        for j in range(n):
            dp[0][j] = j

        for i in range(1, m):
            for j in range(1, n):
                if word2[i] == word1[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1
                    )

        return dp[m - 1][n - 1]


solution = Solution()
word1 = "intention"
word2 = "execution"
print(solution.minDistance(word1, word2))
