class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            n = len(s)
            res += str(n) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        i = 0
        while i < len(s):
            c = s[i]
            if c == '#':
                n = int(s[start:i])
                res.append(s[i + 1:i + 1 + n])
                start = i + 1 + n
                i = start
            else:
                i += 1
        return res




