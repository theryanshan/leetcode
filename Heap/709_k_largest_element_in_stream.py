# Time: heapify O(n), add O(logn), peek O(1)
# Tip: We only need to keep k elements in the heap, so we can use a min heap to store the k largest elements, and that element is at minHeap[0]

import heapq


class KthLargest:
    minHeap = []
    k = 0

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
