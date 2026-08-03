class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lptr = 0
        rptr = len(nums) - 1

        while lptr <= rptr:
            mid = (lptr + rptr) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < nums[rptr]:
                if target < nums[mid]:
                    rptr = mid - 1
                elif target <= nums[rptr]:
                    lptr = mid + 1
                else:
                    rptr =  mid - 1
            else:
                if target > nums[mid]:
                    lptr = mid + 1
                elif target >= nums[lptr]:
                    rptr = mid - 1
                else:
                    lptr = mid + 1
        
        return -1
