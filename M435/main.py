class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[1])
        k = float("-inf")
        counter = 0
        for i in intervals:
            s = i[0]
            f = i[1]
            if s >= k:
                k = f
            else:
                counter += 1

        return counter


solution = Solution()
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(solution.eraseOverlapIntervals(intervals))
