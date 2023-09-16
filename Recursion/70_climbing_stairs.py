# Time: O(2^n)
# Space: O(n)


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.helper(n, memo)

    def helper(self, n, memo):
        if n < 0:
            return 0
        if n == 1 or n == 0:
            return 1
        if n in memo:
            return memo[n]
        left = self.climbStairs(n - 1)
        right = self.climbStairs(n - 2)
        memo[n] = left + right
        return left + right


res = Solution().climbStairs(40)
print(res)
