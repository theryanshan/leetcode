# Time klogn
# Tip: heappush([dist, x, y]), and it will sort by dist by default

import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for x, y in points:
            distance = x**2 + y**2
            minHeap.append([distance, x, y])
        heapq.heapify(minHeap)

        while k > 0:
            item = heapq.heappop(minHeap)
            res.append([item[1], item[2]])
            k -= 1

        return res
