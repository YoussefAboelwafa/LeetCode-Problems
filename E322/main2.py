# Top Down
class Solution(object):
    MAX = 20000

    def coinChange(self, coins, amount):
        memo = [self.MAX] * (amount + 1)
        memo[0] = 0

        def dp(memo, x):
            if memo[x] < self.MAX:
                return memo[x]

            for c in coins:
                if x >= c:
                    sub_problem = dp(memo, x - c)
                    if sub_problem != -1:
                        memo[x] = min(memo[x], sub_problem + 1)
            return memo[x] if memo[x] < self.MAX else -1

        return dp(memo, amount)


solution = Solution()
list = [1,2,5]
print(solution.coinChange(list, 11))
