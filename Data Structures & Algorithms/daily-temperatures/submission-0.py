class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for i,t in enumerate(temperatures):
            while stack and t> stack[-1][1]:
                stackin , stacktemp = stack.pop()
                res[stackin] = i - stackin
            stack.append((i,t))
        return res