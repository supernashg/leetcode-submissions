class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        root = list(range(n))
        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]
        count = n
        for u, v in edges:
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            root[pu] = pv
            count -= 1

        return count == 1