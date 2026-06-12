class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j,res= 0,len(heights)-1,0
        
        while i < j:
            area = (j-i) * min(heights[i],heights[j])
            res = max(res,area)
            if heights[i] > heights[j]:
                j -=1
            else:
                i+=1
        return res