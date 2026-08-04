class Solution:
    def findMin(self, nums: List[int]) -> int:
        # use binary search to find the split
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] <= nums[r]:
                r = mid
            else:
                l = mid + 1
        
        return nums[l]
        