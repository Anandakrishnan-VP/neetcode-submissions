class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for i in strs:
            count =[0]*26

            for w in i:
                count[ord(w) - ord('a')] +=1

            res[tuple(count)].append(i)

        return list(res.values())

