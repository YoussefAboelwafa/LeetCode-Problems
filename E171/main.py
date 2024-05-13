class Solution(object):
    def titleToNumber(self, columnTitle):
        ans = 0
        for char in columnTitle:
            ans = (ans * 26) + ord(char) - ord("A") + 1
        return ans


solution = Solution()
print(solution.titleToNumber("A"))  # 1
print(solution.titleToNumber("AB"))  # 28
print(solution.titleToNumber("ZY"))  # 701
