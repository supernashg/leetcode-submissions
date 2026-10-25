class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for x in nums:
            if x in unique:
                return True
            unique.add(x)

        return False
        