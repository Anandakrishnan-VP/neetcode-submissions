class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k=0
        for i in range(len(nums)):
            for s in nums:
                if s==val:
                    nums.remove(s)
            k=len(nums)
        return k

                    
            