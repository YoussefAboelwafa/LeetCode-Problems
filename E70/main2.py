# Bottom Up
class Solution(object):
    def climbStairs(self, n):
        memo = {}
        memo[0] = 1
        memo[1] = 1
        for i in range(2,n+1):
            memo[i] = memo[i-1] + memo [i-2]
        return memo[n]


solution = Solution()
print(solution.climbStairs(7))
