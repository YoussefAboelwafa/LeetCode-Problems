class Solution(object):
    def findRelativeRanks(self, score):
        ans = ["0"] * len(score)
        dict = {}

        for i in range(len(score)):
            dict[score[i]] = i

        sorted_dict = sorted(dict.keys(), reverse=True)

        for i in range(len(sorted_dict)):
            if i == 0:
                ans[dict[sorted_dict[i]]] = "Gold Medal"
            elif i == 1:
                ans[dict[sorted_dict[i]]] = "Silver Medal"
            elif i == 2:
                ans[dict[sorted_dict[i]]] = "Bronze Medal"
            else:
                ans[dict[sorted_dict[i]]] = str(i+1)

        return ans


solution = Solution()
print(
    solution.findRelativeRanks([5, 4, 3, 2, 1])
)  # ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
print(
    solution.findRelativeRanks([10, 3, 8, 9, 4])
)  # ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
