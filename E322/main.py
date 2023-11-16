# Bottom Up
class Solution(object):
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        memo = [amount + 10] * (amount + 1)
        memo[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if c <= a:
                    memo[a] = min(memo[a], 1 + memo[a - c])

        print(memo)
        return memo[amount] if (memo[amount] != amount + 10) else -1


solution = Solution()
list = [1]
print(solution.coinChange(list, 1))
