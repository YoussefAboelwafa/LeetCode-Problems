import heapq
from collections import Counter, deque


class Solution(object):
    # Max Priority Queue
    class PriorityQueue(object):
        def __init__(self):
            self.queue = []

        def push(self, item):
            # Invert the item value to simulate a max heap
            heapq.heappush(self.queue, -item)

        def pop(self):
            # Invert the popped value back to its original value
            return -heapq.heappop(self.queue)

        def is_empty(self):
            return len(self.queue) == 0

        def size(self):
            return len(self.queue)

    def leastInterval(self, tasks, n):
        time = 0
        q = deque()
        pq = self.PriorityQueue()
        freq = list(Counter(tasks).values())
        for i in freq:
            pq.push(i)

        while True:
            time += 1
            if pq.size() != 0:
                cnt = pq.pop()
                if cnt > 1:
                    q.append([cnt - 1, time + n])

            while len(q) != 0 and q[0][1] <= time:
                pq.push(q.popleft()[0])

            if pq.is_empty() and len(q) == 0:
                break
        return time


solution = Solution()
print(solution.leastInterval(["A", "A", "A", "B", "B", "B"], 2))  # Output: 8
print(solution.leastInterval(["A", "A", "A", "B", "B", "B"], 0))  # Output: 6
print(solution.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))  # Output: 16
