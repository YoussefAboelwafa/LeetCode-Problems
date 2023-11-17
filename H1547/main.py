class Solution(object):
    def minCost(self, n, cuts):
        cuts = [0] + cuts + [n]
        cuts.sort()
        length = len(cuts)

        dp = [[float("inf")] * length for _ in range(length)]

        for d in range(1, length):
            for i in range(length - d):
                j = i + d
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], cuts[j] - cuts[i] + dp[i][k] + dp[k][j])
                if dp[i][j] == float("inf"):
                    dp[i][j] = 0
        for i in range(length):
            print(dp[i])
        return dp[0][length - 1]


solution = Solution()
cuts = [1, 3, 4, 5]
print(solution.minCost(7, cuts))
