class Solution(object):
    def findDifference(self, nums1, nums2):
        ans = [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]
        return ans


solution = Solution()
print(solution.findDifference([1, 2, 3], [2, 4, 6]))  # [[1, 3], [4, 6]]
