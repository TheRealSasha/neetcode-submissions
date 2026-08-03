class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pre-process
        L = []

        for c in s:
            if c.isalpha():
                L.append(c.lower())
            elif c.isdecimal():
                L.append(c)

        lptr = 0
        rptr = len(L) - 1

        while lptr < rptr:
            if L[lptr] != L[rptr]:
                return False
            
            lptr += 1
            rptr -= 1
        
        return True




        