class Solution(object):
    def insert(self, intervals, newInterval):
        result = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        result.append(newInterval)
        return result


solution = Solution()
print(solution.insert([[1, 3], [6, 9]], [2, 5]))  # Output: [[1, 5], [6, 9]]
print(solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))  # Output: [[1, 2], [3, 10], [12, 16]]
