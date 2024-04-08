class Solution(object):
    
    def rotate(self, list):
        if list:
            head = list.pop(0)
            list.append(head)
        return list
    
    def countStudents(self, students, sandwiches):
        n = len(students)
        counter = n
        while(counter and len(students) != 0):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                counter = n
            else:
                self.rotate(students)
            counter-= 1
        return len(students)
        
        
solution = Solution()
print(solution.countStudents([1,1,0,0], [0,1,0,1])) # 0
print(solution.countStudents([1,1,1,0,0,1], [1,0,0,0,1,1])) # 3