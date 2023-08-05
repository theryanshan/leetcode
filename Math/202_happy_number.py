# Keep adding the sum of squares of digits until the number becomes 1 or the number is already seen
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            if n == 1:
                return True
            n = self.getSumOfDigits(n)
        return False

    def getSumOfDigits(self, n):
        sum = 0
        while n > 0:
            sum += pow(n % 10, 2)
            n //= 10
        return sum


s = Solution()
ans = s.isHappy(2)
print(ans)
