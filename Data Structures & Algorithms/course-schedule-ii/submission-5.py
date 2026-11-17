class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(node):

            for child in graph[node]:
                indeg[child] -= 1
                if indeg[child] == 0:
                    orders.append(child)
                    indeg[child] = -1
                    dfs(child)
                    
        
        graph = defaultdict(list)
        indeg = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1
        orders = []

        for i in range(numCourses):
            if indeg[i] == 0:
                orders.append(i)
                indeg[i] = -1
                dfs(i)
        #print(orders)
        return orders if len(orders) == numCourses else []
