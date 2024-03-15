class Solution(object):
    def productExceptSelf(self, nums):
        zero_counter = 0
        total_product = 1
        ans = [0] * len(nums)

        for num in nums:
            if num != 0:
                total_product *= num
            else:
                zero_counter += 1

        for i in range(len(nums)):
            if zero_counter > 1:
                ans[i] = 0
            elif zero_counter == 1:
                if nums[i] == 0:
                    ans[i] = total_product
            else:
                ans[i] = total_product // nums[i]

        return ans


solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))  # [24,12,8,6]
print(solution.productExceptSelf([0, 0]))  # [0,0]
