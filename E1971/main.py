from collections import deque


class Solution(object):
    def validPath(self, n, edges, source, destination):

        adj = {}
        for edge in edges:
            if edge[0] not in adj:
                adj[edge[0]] = []
            adj[edge[0]].append(edge[1])
            if edge[1] not in adj:
                adj[edge[1]] = []
            adj[edge[1]].append(edge[0])

        visited = [False] * n
        queue = deque([source])

        while queue:
            node = queue.popleft()
            
            if node == destination:
                return True
            
            if not visited[node]:
                visited[node] = True
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        queue.append(neighbor)

        return False


solution = Solution()
print(solution.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))  # True
print(solution.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5))  # False
