class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        ans = sorted(set(nums))

        for i,w in enumerate(ans):
            nums[i] = w
        return len(ans)