class Solution:


    def validPalindrome(self, s: str) -> bool:
        def isplaindrome(i, j):
            while i<j:
                if s[i] != s[j]:
                    return False
                i += 1
                j-= 1

            return True

        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                l = isplaindrome(i + 1, j)
                r = isplaindrome(i, j - 1)
                return l or r
            i += 1
            j -= 1
        return True
