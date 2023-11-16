# Divide & Conquer
class Solution(object):
    neg_inf = float("-inf")

    def maxSubArray(self, nums):
        return self.find_max_subarray(nums, 0, len(nums) - 1)

    def find_max_subarray(self, A, l, h):
        if l == h:
            return A[l]
        else:
            mid = (l + h) // 2
            left_sum = self.find_max_subarray(A, l, mid)
            right_sum = self.find_max_subarray(A, mid + 1, h)
            cross_sum = self.find_max_crossing_subarray(A, l, mid, h)
            return max(left_sum, right_sum, cross_sum)

    def find_max_crossing_subarray(self, A, l, mid, h):
        left_sum = self.neg_inf
        sum = 0
        for i in range(mid, l - 1, -1):
            sum += A[i]
            if left_sum < sum:
                left_sum = sum

        right_sum = self.neg_inf
        sum = 0
        for i in range(mid + 1, h + 1):
            sum += A[i]
            if right_sum < sum:
                right_sum = sum

        return left_sum + right_sum


solution = Solution()
nums = [5, 4, -1, 7, 8]
print(solution.maxSubArray(nums))
