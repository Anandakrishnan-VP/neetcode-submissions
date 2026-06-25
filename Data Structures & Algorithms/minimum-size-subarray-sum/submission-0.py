class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        res = 0
        i = 0
        j = 0
        length = float('inf')
        while i<=j and j< len(nums):
            res += nums[j]

            while res >= target:
                l = (j+1) -i
                length = min(length,l)
                res -= nums[i]
                i += 1
            j += 1

                

        return 0 if length == float('inf') else  length
            