class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        buckets = [[] for _ in range(len(nums))]

        for num, freq in cnt.items():
            buckets[freq - 1].append(num)
        
        found = k
        idx = len(nums) - 1
        res =[]
        
        while k > 0:
            if buckets[idx]:
                if len(buckets[idx]) > k:
                    res.extend(buckets[idx][:k])
                    k = 0
                else:
                    res.extend(buckets[idx])
                    k -= len(buckets[idx])
            idx -= 1

        return res

        