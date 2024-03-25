class Solution(object):
    def findDuplicates(self, nums):
        duplicates = []
        hash_set = set()
        for i in nums:
            if i in hash_set:
                duplicates.append(i)
            else:
                hash_set.add(i)
        return duplicates
        
        
solution = Solution()
print(solution.findDuplicates([4,3,2,7,8,2,3,1])) # [2,3]
print(solution.findDuplicates([1,1,2])) # [1]
print(solution.findDuplicates([1,2,3])) # []
