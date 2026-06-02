class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        t_list = list(t)
        s_list = list(s)
        for char in s:
            if char in t_list:
                t_list.remove(char)
            else:   
                return False
        return True
