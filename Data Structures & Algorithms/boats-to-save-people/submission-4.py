class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i,j,boat=0,len(people)-1,0

        people.sort()
        while i<=j:
                if people[j] == limit:
                    boat +=1
                    j -=1
                elif people[i] + people[j] > limit:
                    boat+=1
                    j -=1
                else:
                    boat +=1
                    i +=1
                    j -=1
            # else:
            #     boat += 1
            #     i+=1
            #     j-=1
                
        
        return boat        
            
