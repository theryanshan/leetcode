# Time: O(n)
# Space: O(1)
# Two pointers, one from left, one from right, skip non-alphanumeric characters if l < r


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while not self.isalnum(s[l]) and l < r:
                l += 1
            while not self.isalnum(s[r]) and l < r:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def isalnum(self, ch: str) -> bool:
        return (
            ord(ch) >= ord("A")
            and ord(ch) <= ord("Z")
            or ord(ch) >= ord("a")
            and ord(ch) <= ord("z")
            or ord(ch) >= ord("0")
            and ord(ch) <= ord("9")
        )
