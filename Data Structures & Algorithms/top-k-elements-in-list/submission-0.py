from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count = Counter(nums)
        for key in count:

            heapq.heappush(heap, (-count[key], key))
            
        res = []
        while k:
            res.append(heapq.heappop(heap)[1])
            k -= 1

        return res
