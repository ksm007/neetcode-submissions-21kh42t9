class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
                heapq.heappush(self.minHeap,num)
        else:
            heapq.heappush(self.maxHeap,-1 * num)
        # blancing the length
        if len(self.minHeap) > len(self.maxHeap) +1:
            ele = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * ele)
        if len(self.maxHeap) > len(self.minHeap) +1:
            ele = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, ele)

        

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        if len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]
        return (-1 * self.maxHeap[0] + self.minHeap[0]) / 2.0

        