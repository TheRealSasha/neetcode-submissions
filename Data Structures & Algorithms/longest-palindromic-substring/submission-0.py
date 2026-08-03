class Solution:
    def longestPalindrome(self, s: str) -> str:
        # for each index, check for a palindrome whose center is the index; account for even and odd lenght palindromes
        n = len(s)
        best_l, best_r = 0, 0 

        for i in range(n):
            # even center
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            
            if r - l > best_r - best_l:
                best_r = r
                best_l = l
    
            # odd center 
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            if r - l > best_r - best_l:
                best_r = r
                best_l = l

        return s[best_l + 1:best_r]

    