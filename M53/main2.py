class Solution(object):
    neg_inf = float("-inf")

    def maxSubArray(self, nums):
        max_sum = 0
        curr_sum = 0

        for i in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += i
            max_sum = max(max_sum, curr_sum)
            
        return max_sum


solution = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(solution.maxSubArray(nums))
