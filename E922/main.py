class Solution(object):
    def sortArrayByParityII(self, nums):
        i = 0  # even pointer
        j = 1  # odd pointer
        n = len(nums)

        while i < n and j < n:
            while i < n and nums[i] % 2 == 0:
                i += 2
            while j < n and nums[j] % 2 == 1:
                j += 2
            if i < n and j < n:
                nums[i], nums[j] = nums[j], nums[i]

        return nums


solution = Solution()
nums = [4, 2, 5, 7]
print(solution.sortArrayByParityII((nums)))
