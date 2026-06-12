class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #using rev

        k = k % len(nums)
        n = len(nums)-1
        

        def ro(l,r):
            while l<r:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                r-=1
                
        ro(0,n)
        ro(0,k-1)
        ro(k,n)
    
       
        
    