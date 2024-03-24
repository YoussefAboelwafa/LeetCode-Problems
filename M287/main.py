class Solution(object):
    def findDuplicate(self, nums):
        hash_set = set()
        
        for i in nums:
            if i in hash_set:
                return i
            hash_set.add(i)
        
        
solution = Solution()
print(solution.findDuplicate([1,3,4,2,2])) # 2
print(solution.findDuplicate([3,1,3,4,2])) # 3
print(solution.findDuplicate([3,3,3,3,3])) # 3