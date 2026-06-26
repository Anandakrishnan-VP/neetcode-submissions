class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return  ""
        hasht = {}
        hashw = {}
        
        resl = float("infinity")
        res = [-1,-1]

        for ch in t:
            hasht[ch] = 1 + hasht.get(ch,0)
        i= 0
        have,need= 0 , len(hasht)
        for r in range(len(s)):
            c = s[r]
            hashw[c] = 1 + hashw.get(c,0)

            if c in hasht and hasht[c] == hashw[c]:
                have +=1
            
            while have == need:

                if resl > (r-i+1):
                    resl = (r+1) - i 
                    res = [i,r]
                
                hashw[s[i]] -=1
                if s[i] in hasht and hashw[s[i]] < hasht[s[i]]:
                    have -= 1
                i +=1
        i,r = res
        return s[i:r+1] if resl != float("infinity") else ""
        
