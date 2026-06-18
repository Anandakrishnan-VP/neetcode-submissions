class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                chara = ""
                while stack[-1] != "[":
                    chara = stack.pop() + chara
                stack.pop()
                n = ""
                while stack and stack[-1].isdigit():
                    n = stack.pop() + n
                stack.append(int(n)*chara)
        return "".join(stack) 