class Solution(object):
    def insert(self, intervals, newInterval):
        result = []

        # 3 cases for newInterval:
        # 1. New interval is before the current interval
        # 2. New interval is after the current interval
        # 3. New interval overlaps with the current interval

        for i in range(len(intervals)):

            # New interval is before the current interval
            # If newInterval[1] < intervals[i][0], then newInterval is before intervals[i]
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]

            # New interval is after the current interval
            # If newInterval[0] > intervals[i][1], then newInterval is after intervals[i]
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])

            # New interval overlaps with the current interval
            # If newInterval[1] >= intervals[i][0] and newInterval[0] <= intervals[i][1], then there is an overlap
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        result.append(newInterval)
        return result


solution = Solution()
print(solution.insert([[1, 3], [6, 9]], [2, 5]))  # Output: [[1, 5], [6, 9]]
print(solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))  # Output: [[1, 2], [3, 10], [12, 16]]
