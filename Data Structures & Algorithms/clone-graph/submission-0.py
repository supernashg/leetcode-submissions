"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        maps = {}
        
        def dfs(node):
            if node in maps:
                return maps[node]
            new = Node(node.val)
            maps[node] = new
            for nei in node.neighbors:
                new.neighbors.append(dfs(nei))
            
            return new

        new_node = dfs(node)
        return new_node