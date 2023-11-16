# Top Down
class Solution(object):
    def minCostClimbingStairs(self, cost):
        if len(cost) < 2:
            return min(cost[0], cost[1])
        memo = [1000] * len(cost)
        memo[0] = cost[0]
        memo[1] = cost[1]
        return min(
            self.dp(cost, memo, len(cost) - 1), self.dp(cost, memo, len(cost) - 2)
        )

    def dp(self, cost, memo, n):
        if n == 0 or n == 1:
            return memo[n]
        if memo[n] == 1000:
            memo[n] = min(
                self.dp(cost, memo, n - 1) + cost[n],
                self.dp(cost, memo, n - 2) + cost[n],
            )
        return memo[n]


solution = Solution()
list = [10, 15, 20]
print(solution.minCostClimbingStairs(list))
