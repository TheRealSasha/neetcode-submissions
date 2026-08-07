class MedianFinder:
    def __init__(self):
        self.minheap = [] # store the larger half
        self.maxheap = [] # store the smaller half
        
    def addNum(self, num: int) -> None:
        if not len(self.minheap) and not len(self.maxheap):
            heapq.heappush(self.minheap, num)
        elif self.minheap[0] >= num:
            heapq.heappush_max(self.maxheap, num)

            if len(self.maxheap) > len(self.minheap) + 1:
                heapq.heappush(self.minheap, heapq.heappop_max(self.maxheap))
        else:
            heapq.heappush(self.minheap, num)

            if len(self.minheap) > len(self.maxheap) + 1:
                heapq.heappush_max(self.maxheap, heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return self.maxheap[0]
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return (self.maxheap[0] + self.minheap[0]) / 2
        
        
        