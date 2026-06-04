class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        hash ={}
        size = len(nums)/3
        res=[]


        for n in nums:
            hash[n] = hash.get(n,0)+1
        for key,value in hash.items():
            if value>size:
                res.append(key)
        return res

        
        