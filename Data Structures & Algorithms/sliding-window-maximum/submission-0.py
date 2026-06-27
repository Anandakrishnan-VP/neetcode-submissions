class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        i = 0
        j = k - 1
        while i <= j and j <= len(nums)-1:
            res.append(max(nums[i:j+1]))
            i +=1
            j +=1
        return res
