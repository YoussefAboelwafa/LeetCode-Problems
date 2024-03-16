class Solution(object):
    def findMaxLength(self, nums):
        prefix_sum_index = {0: -1}
        max_len = 0
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += -1 if nums[i] == 0 else 1

            if prefix_sum in prefix_sum_index:
                max_len = max(max_len, i - prefix_sum_index[prefix_sum])
            else:
                prefix_sum_index[prefix_sum] = i

        return max_len


solution = Solution()
print(solution.findMaxLength([0, 0]))  # Output: 2
print(solution.findMaxLength([0, 1, 0]))  # Output: 2