class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        s_counter.subtract(t)

        for v in s_counter.values():
            if v:
                return False
        
        return True
            


            
        


        