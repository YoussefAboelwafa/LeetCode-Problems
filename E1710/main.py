class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        value = 0
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        for box_numbers, box_value in boxTypes:
            if box_numbers <= truckSize:
                value += box_numbers * box_value
                truckSize -= box_numbers
            else:
                value += truckSize * box_value
                break

        return value


solution = Solution()
boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
print(solution.maximumUnits(boxTypes, 10))
