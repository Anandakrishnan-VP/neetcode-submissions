class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {']':'[','}':'{',')':'('}

        for b in s:
            if b in pair:
                if stack and pair[b] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(b)
            else:
                stack.append(b)
        return True if not stack else False
        