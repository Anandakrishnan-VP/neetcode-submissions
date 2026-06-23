class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = set()
        count = 0
        i,r = 0,0
        lc = 0
        while r <= len(s) -1 :
            if s[r] not in m:
                m.add(s[r])
                lc+=1
                r +=1
                count = max (count,lc)
            else:
                m.remove(s[i])
                i += 1
                lc -=1
        return count


        