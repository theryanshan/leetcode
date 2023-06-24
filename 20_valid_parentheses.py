# 20. Valid Parentheses
# Time: O(n)
# Space: O(n)
# Tip: use stack to store open parentheses, use a map to store matching parentheses, the close parentheses are the key, the matching open parentheses are the value


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {")": "(", "}": "{", "]": "["}
        for ch in s:
            if ch in map.values():
                stack.append(ch)
            elif stack and map[ch] == stack[-1]:
                stack.pop()
            else:
                return False
        return not stack


print(Solution().isValid("()("))
