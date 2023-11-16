# Top Down
class Solution(object):
    def climbStairs(self, n):
        memo = {}
        return self.dp(memo, n)
    
    def dp(self, memo, n):
        if n==0 or n ==1:
            return 1
        elif n in memo:
            return memo[n]
        else:
            memo[n] = self.dp(memo, n-1) + self.dp(memo, n-2)
            
        return memo[n]


solution = Solution()
print(solution.climbStairs(7))
