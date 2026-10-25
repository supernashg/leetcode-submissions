class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = {}
        for i in range(len(nums)):
            
            if target - nums[i] in D:
                return [D[target - nums[i]] , i]

            D[nums[i]] = i