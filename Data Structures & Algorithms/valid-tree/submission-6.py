class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = list(range(n))
        component = n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            nonlocal component
            px = find(x)
            py = find(y)
            if px != py:
                parent[px] = py
                component -= 1
                return False
            else:
                return True

        for i, j in edges:
            if union(i, j):
                return False

        return True if component == 1 else False


        