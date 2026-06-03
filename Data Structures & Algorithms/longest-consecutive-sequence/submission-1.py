class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set(nums)
        longest=0

        for n in nums:
            if (n-1) not in numset:
                streak =0

                while (n+streak)  in numset:
                    streak +=1
                longest = max(streak,longest)
        return longest


        
