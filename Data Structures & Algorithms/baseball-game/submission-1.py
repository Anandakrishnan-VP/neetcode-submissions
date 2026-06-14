class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum = 0

        for op in operations:

            if op == 'C':
                stack.pop()
            elif op == 'D':
                val = 2 * stack[-1]
                stack.append(val)
                
            elif op == '+':
                val = stack[-1] + stack[-2]
                stack.append(val)
                
            else :
                val = int(op)
                stack.append(val)
        
        for s in stack:
            sum += s        
        return sum