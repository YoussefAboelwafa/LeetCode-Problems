class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(0, i + 1):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


Solution = Solution()
nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
print(Solution.lengthOfLIS(nums))
