"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        maps = {}
        new_node = Node(node.val)
        maps[node] = new_node
        q = deque([node])
        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in maps:
                    new_nei = Node(nei.val)
                    maps[nei] = new_nei
                    q.append(nei)
                maps[cur].neighbors.append(maps[nei])
        return maps[node]
                


        