class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()
        i=j=0

        while j < len(nums):

            while q and nums[q[-1]] < nums[j]:
                q.pop()
            q.append(j)


            if j + 1 >= k:
                res.append(nums[q[0]])
                i += 1
            j +=1

            if i > q[0]:
                q.popleft()



        return res