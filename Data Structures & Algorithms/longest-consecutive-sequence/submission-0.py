class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums = set(nums)

        while len(nums):
            l = r = nums.pop()
            cur = 1

            while l - 1 in nums:
                cur += 1
                l -= 1
                nums.remove(l)
            while r + 1 in nums:
                cur += 1
                r += 1
                nums.remove(r)
            ans = max(ans, cur)
            
        return ans