class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if not words:
            return ''

        graph = defaultdict(set)
        indeg = {}
        for w in words:
            for c in w:
                indeg[c] = 0

        for x, y in zip(words, words[1:]):
            # Check for invalid prefix condition: "wrtkj" before "wrt"
            if len(x) > len(y) and x.startswith(y):
                return ""
            for a, b in zip(x, y):
                if a != b:
                    if b not in graph[a]:
                        graph[a].add(b)
                        indeg[b] += 1
                    break
        res = []
        q = deque([k for k, v in indeg.items() if v == 0])
        while q:
            node = q.popleft()
            res.append(node)
            for child in graph[node]:
                indeg[child] -= 1
                if indeg[child] == 0:
                    q.append(child)
        
        # If res doesn't contain all unique characters, there was a cycle
        return ''.join(res) if len(res) == len(indeg) else ""