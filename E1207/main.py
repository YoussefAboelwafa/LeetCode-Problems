from collections import Counter


class Solution(object):
    def uniqueOccurrences(self, arr):
        dict = Counter(arr)
        count_set = set()
        for i in dict.values():
            if i in count_set:
                return False
            else:
                count_set.add(i)
        return True


solution = Solution()
arr = [1, 2, 2, 1, 1, 3]
print(solution.uniqueOccurrences(arr))
