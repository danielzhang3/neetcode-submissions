class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        if self.right and -self.left[0] > self.right[0]: 
            x = -heapq.heappop(self.left)
            heapq.heappush(self.right, x)
        
        if len(self.left) > len(self.right) + 1: 
            x = -heapq.heappop(self.left)
            heapq.heappush(self.right, x)
        elif len(self.right) > len(self.left): 
            x = -heapq.heappop(self.right)
            heapq.heappush(self.left, x)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right): 
            return -self.left[0]
        else: 
            return (-float(self.left[0]) + float(self.right[0])) / 2.0
        
        