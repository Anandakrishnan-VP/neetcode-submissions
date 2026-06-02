class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash={}
        freq=[[] for _ in range(len(nums)+1)]

        #build the hashmap
        for num in nums:
            hash[num] = 1 + hash.get(num,0)

        #build freq array 
        for n,c in hash.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res