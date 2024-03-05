class Solution(object):
    def largestAltitude(self, gain):
        acc_sum = 0
        max_gain = 0
        for i in gain:
            acc_sum += i
            max_gain = max(max_gain, acc_sum)
        return max_gain


solution = Solution()
gain = [-4,-3,-2,-1,4,3,2]
print(solution.largestAltitude(gain))
