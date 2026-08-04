class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # do it in one pass
        n = len(nums)
        prefix = [1] * n
        postfix = 1

        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        
        for i in range(n - 1, -1, -1):
            prefix[i] *= postfix
            postfix *= nums[i]
        
        return prefix


        


        