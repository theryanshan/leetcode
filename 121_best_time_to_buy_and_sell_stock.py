# Time: O(n)
# Space: O(1)
# Two pointers, l is always pointing at the lowest price so far, update max_profit if possible
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
            r += 1
        return max_profit
