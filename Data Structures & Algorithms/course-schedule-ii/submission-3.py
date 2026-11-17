class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indeg = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1
        orders = []
        q = deque()
        for i, x in enumerate(indeg):
            if x == 0:
                q.append(i)
        while q:
            node = q.popleft()
            orders.append(node)

            for child in graph[node]:
                indeg[child] -= 1
                if indeg[child] == 0:
                    q.append(child)


        return orders if len(orders) == numCourses else []
