class Solution(object):
    def findMaxAverage(self, nums, k):
        n = len(nums)
        window_sum = float(sum(nums[:k]))
        max_avg = float(window_sum / k)
        for i in range(k, n):
            window_sum = float(window_sum) + nums[i] - nums[i - k]
            cur_avg = float(window_sum / k)
            max_avg = max(max_avg, cur_avg)
        return float(max_avg)


solution = Solution()
nums = [1, 12, -5, -6, 50, 3]
k = 4
print(solution.findMaxAverage(nums, k))
