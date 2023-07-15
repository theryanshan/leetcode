# Time: O(n) + O(log(n)) heapify + heapify pop


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = -1 * heapq.heappop(stones)
            second = -1 * heapq.heappop(stones)
            remain = first - second
            if remain > 0:
                heapq.heappush(stones, -1 * remain)
        heapq.heappush(stones, 0)
        return -1 * heapq.heappop(stones) if len(stones) == 1 else 0
