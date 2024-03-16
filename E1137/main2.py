# Top-Down Approach
class Solution(object):
    def tribonacci(self, n):
        dp = [-1] * (n + 1)

        def fib(n):
            if dp[n] != -1:
                return dp[n]
            if n < 2:
                return n
            elif n == 2:
                return 1
            else:
                dp[n] = fib(n - 1) + fib(n - 2) + fib(n - 3)
                return dp[n]

        return fib(n)


solution = Solution()
print(solution.tribonacci(3))
