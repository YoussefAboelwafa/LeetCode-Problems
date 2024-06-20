class Solution(object):
    def isAnagram(self, s, t):
        
        if len(s) != len(t):
            return False
        
        count_s, count_t = {}, {}
        
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        
        return count_s == count_t
        
        
solution = Solution()
print(solution.isAnagram("anagram", "nagaram")) # True
print(solution.isAnagram("rat", "car")) # False