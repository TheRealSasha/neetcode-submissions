class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()

        for i, v in enumerate(nums):
            diff = target - v

            if diff in d:
                return [d[diff], i]
            
            d[v] = i
        
        return []
