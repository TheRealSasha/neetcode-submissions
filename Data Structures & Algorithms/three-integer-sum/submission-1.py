class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        numss = sorted(nums)
        seen = set()
        res = []

        for i in range(n):
            if numss[i] > 0:
                break

            if numss[i] not in seen:
                self.twoSum(numss, i, -numss[i], res)

            seen.add(numss[i])

        return res
    
    def twoSum(self, nums, start, total, res):
        n = len(nums)
        lptr = start + 1
        rptr = n - 1

        while lptr < rptr:
            if nums[lptr] > total // 2:
                break
            curr = nums[lptr] + nums[rptr]
            if curr == total:
                res.append([nums[start], nums[lptr], nums[rptr]])

                lptr += 1
                rptr -= 1

                while lptr < n and nums[lptr] == nums[lptr - 1]:
                    lptr += 1

                while rptr >= 0 and nums[rptr] == nums[rptr + 1]:
                    rptr -= 1

            elif curr < total:
                lptr += 1
            else:
                rptr -= 1

        

        
            


            
        