import heapq


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
