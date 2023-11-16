# Top Down
class Solution(object):
    def fibonacci(self,n,memo):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n in memo:
            return memo[n]
        else:
            memo[n] = self.fibonacci(n - 1, memo) + self.fibonacci(n - 2, memo)
        return memo[n]
    
    def fib(self, n):
       memo={}
       ans = self.fibonacci(n,memo)
       return ans
        
                
        
solution = Solution()
print(solution.fib(30))
