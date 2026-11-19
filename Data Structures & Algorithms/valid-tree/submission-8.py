from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
            
        graph = defaultdict(list)
        visit = [0] * n
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def has_circle(node, parent):
            if visit[node] == 1:
                return True

            visit[node] = 1
            for child in graph[node]:
                if child == parent:
                    continue
                if has_circle(child, node):
                    return True
            return False

        return not has_circle(0, -1) and all(v == 1 for v in visit)

