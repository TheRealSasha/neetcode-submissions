class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lptr = 0
        rptr = len(heights) - 1
        res = 0

        while lptr < rptr:
            res = max(res, (rptr - lptr) * min(heights[lptr], heights[rptr]))
            
            if heights[lptr] < heights[rptr]:
                lptr += 1
            else:
                rptr -= 1
        
        return res


        