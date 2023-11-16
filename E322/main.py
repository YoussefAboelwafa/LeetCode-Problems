# Bottom Up
class Solution(object):
    MAX = 20000

    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        memo = [self.MAX] * (amount + 1)
        memo[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if c <= a:
                    memo[a] = min(memo[a], 1 + memo[a - c])
        return memo[amount] if (memo[amount] != self.MAX) else -1


solution = Solution()
list = [1,2,5]
print(solution.coinChange(list, 11))
