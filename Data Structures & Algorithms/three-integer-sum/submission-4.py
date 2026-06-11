class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for k, t in enumerate(nums):
            if t>0:
                break
            if k > 0 and t == nums[k - 1]:
                continue

            i, j = k + 1, len(nums) - 1

            while i < j  :
                if nums[i] + nums[j] > -t:
                    j -= 1
                elif nums[i] + nums[j] < -t:
                    i += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    i +=1
                    j -=1
                    while i<j and nums[i] == nums[i-1]:
                        i +=1
                    while j>i and nums[j] == nums[j+1]:
                        j -=1
        return res
