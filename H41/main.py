class Solution(object):
    def firstMissingPositive(self, nums):
        for i, value in enumerate(nums):
            if value < 0:
                nums[i] = 0
                
        for i in range(len(nums)):
            val = abs(nums[i])
            
            if 1 <= val <= len(nums):
                
                if nums[val -1] > 0:
                    nums[val-1] *= -1
            
                elif nums[val-1] == 0:
                    nums[val-1] = -1 * (len(nums) + 1) 
        
        for i in range(1,len(nums) + 1):
            if nums[i-1] >= 0:
                return i
                  
        return len(nums) + 1
        
        
solution = Solution()
print(solution.firstMissingPositive([1,2,0])) # 3
print(solution.firstMissingPositive([3,4,-1,1])) # 2
print(solution.firstMissingPositive([7,8,9,11,12])) # 1