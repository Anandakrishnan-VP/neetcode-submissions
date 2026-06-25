class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        l = 0
        r = len(s1)
        while l < r and r <= len(s2):
            if Counter(s2[l:r:1]) == target:
                return True
            else:
                l +=1
                r +=1
        return False
        

        