class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = len(nums)
        k= k%l
        nums[:]= nums[l-k:l:1]+nums[0:l-k:1]
    