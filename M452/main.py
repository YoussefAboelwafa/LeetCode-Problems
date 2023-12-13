class Solution(object):
    def findMinArrowShots(self, points):
        points = sorted(points, key=lambda x: x[1])
        for row in points:
            print(row)
        k = float("-inf")
        counter = 0

        for p in points:
            s = p[0]
            f = p[1]
            if s > k:
                counter += 1
                k = f
        return counter


solution = Solution()
points = [[10, 16], [2, 8], [1, 6], [7, 12]]
print(solution.findMinArrowShots(points))
