class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        l = 0
        for r in range(len(prices)):
            if prices[r] > prices[l]:
                p = max(p, prices[r]-prices[l])
                
            else:
                l = r
        return p
            