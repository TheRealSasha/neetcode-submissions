class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        even = []

        for i, v in enumerate(nums):
            if target % 2 == 0 and v == target // 2:
                even.append(i)
            else:
                d[v] = i

        if len(even) > 1:
            return even[:2]

        for v, i in d.items():
            if target - v in d:
                return sorted([i, d[target - v]])
        
        return [] 