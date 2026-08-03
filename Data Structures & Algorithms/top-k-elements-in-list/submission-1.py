class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        buckets = [[] for _ in range(len(nums))]

        for num, freq in cnt.items():
            buckets[freq - 1].append(num)
        
        found = k
        idx = len(nums) - 1
        res = []
        
        while k > 0:
            if buckets[idx]:
                bound = min(k, len(buckets[idx]))
                res.extend(buckets[idx][:bound])
                k -= bound
            idx -= 1

        return res

        