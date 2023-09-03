# n & 1 always get the right most bit of n, n >> 1 is n // 2
# O(1) time, O(1) space


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            cur = n & 1
            count += cur
            n = n >> 1
        return count


sol = Solution()
ans = sol.hammingWeight(11)
print(ans)
