class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=""
        i,j=0,0
        s1=len(word1)
        s2=len(word2)

        while i<s1 and j<s2:
            s +=(word1[i])
            s +=(word2[j])
            i+=1
            j+=1
        
        s+=(word1[i:])
        s+=(word2[j:])
        return s


        
        

   

                
           
        
        
