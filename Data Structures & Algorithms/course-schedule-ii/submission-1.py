class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        visit = [0] * numCourses
        for a, b in prerequisites:
            graph[a].append(b)

        orders = []

        def has_circle(node):
            if visit[node] == 1:
                return True
            if visit[node] == 2:
                return False

            visit[node] = 1
            for child in graph[node]:
                if has_circle(child):
                    return True
            visit[node] = 2
            orders.append(node)
            return False

        for i in range(numCourses):
            if has_circle(i):
                return []
        return orders
