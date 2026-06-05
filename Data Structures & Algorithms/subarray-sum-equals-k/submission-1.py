class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefixsum

        res = 0
        cursum = 0
        presum = { 0 : 1}
        for n in nums:
            cursum += n
            diff = cursum - k
            res += presum.get(diff,0)
            presum[cursum] = presum.get(cursum,0) + 1
        return res