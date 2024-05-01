class Solution(object):
    def reversePrefix(self, word, ch):
        if ch not in word:
            return word
        ans = word[: word.index(ch) + 1][::-1] + word[word.index(ch) + 1 :]
        return ans


solution = Solution()
print(solution.reversePrefix("abcdef", "d"))  # "dcbaef"
