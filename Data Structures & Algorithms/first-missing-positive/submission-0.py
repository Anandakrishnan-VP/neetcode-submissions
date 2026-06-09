class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        target = 1
        for num in nums:
            if num == target:
                target +=1
        return target