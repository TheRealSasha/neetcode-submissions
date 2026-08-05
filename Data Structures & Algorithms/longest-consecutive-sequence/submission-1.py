class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0

        for num in s:
            if num - 1 not in s:
                curr_best = 1

                while num + curr_best in s:
                    curr_best += 1
                
                best = max(curr_best, best)
        
        return best

        