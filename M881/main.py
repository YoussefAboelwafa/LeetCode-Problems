class Solution(object):
    def numRescueBoats(self, people, limit):
        counter = 0
        start = 0
        end = len(people) - 1
        people.sort()
        
        while end - start > 0:
            
            if people[start] + people[end] <= limit:
                start += 1
                end -= 1
                counter += 1
                
            elif people[start] + people[end] > limit:
                end -= 1
                counter += 1
                
            if start == end:
                counter += 1
                break
        
        return counter


solution = Solution()
print(solution.numRescueBoats([1, 2], 3))  # 1
print(solution.numRescueBoats([3, 2, 2, 1], 3))  # 3
print(solution.numRescueBoats([3, 5, 3, 4], 5))  # 4
