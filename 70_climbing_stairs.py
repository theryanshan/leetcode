# Time: O(n)
# Space: O(1)
# Tip: the count for current step is the sum of previous two steps
# base case: 0 step, 1 way; 1 step, 1 way
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(2, n + 1, 1):
            temp = two
            two = two + one
            one = temp
        return two
