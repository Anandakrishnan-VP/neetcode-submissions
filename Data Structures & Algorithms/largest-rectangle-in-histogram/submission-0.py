class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0

        for i in range(len(heights)):
            j,h = i-1,i+1
            count = 1
            while j>=0 and heights[j] >= heights[i] :
                j -=1
                count +=1
            while h<= len(heights)-1 and heights[h] >= heights[i]:
                h +=1
                count +=1
            area = max (area, heights[i] * count)

        return area

            
        