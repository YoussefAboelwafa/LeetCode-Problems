class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        X = "0" + text1
        Y = "0" + text2
        m = len(X)
        n = len(Y)
        dp = [[0] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                if X[i] == Y[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m - 1][n - 1]


Solution = Solution()
text1 = "abcbd"
text2 = "bdcab"
print(Solution.longestCommonSubsequence(text1, text2))
