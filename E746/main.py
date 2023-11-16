# Bottom Up
class Solution(object):
    def minCostClimbingStairs(self, cost):
        if len(cost) == 2:
            return min(cost[0], cost[1])
        memo = [1000] * len(cost)
        memo[0] = cost[0]
        memo[1] = cost[1]
        for c in range(2, len(cost)):
            memo[c] = min(memo[c - 2] + cost[c], memo[c - 1] + cost[c])

        return min(memo[-1], memo[-2])


solution = Solution()
list = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(solution.minCostClimbingStairs(list))
