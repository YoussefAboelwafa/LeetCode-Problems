# Bottom-Up Approach
class Solution(object):
    def tribonacci(self, n):
        if n < 2:
            return n
        elif n == 2:
            return 1
        else:
            memo = [0] * (n + 1)
            memo[0] = 0
            memo[1] = 1
            memo[2] = 1
            for i in range(3, n + 1):
                memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
            return memo[n]


solution = Solution()
print(solution.tribonacci(25))
