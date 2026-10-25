import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = collections.defaultdict(list)

        for string in strs:
            count = [0] * 26
            for s in string:
                ix = ord(s) - ord('a')
                count[ix] += 1
            group[tuple(count)].append(string)

        return list(group.values())

        