class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        visit = defaultdict(int)
        for a, b in prerequisites:
            g[a].append(b)
        

        def dfs(node):
            if visit[node] == 1:
                return True
            if visit[node] == 2:
                return False

            visit[node] = 1
            for child in g[node]:
                if dfs(child):
                    return True
                
            visit[node] = 2
            return False

        for i in list(g):
            if dfs(i):
                return False

        return True
            

            

        