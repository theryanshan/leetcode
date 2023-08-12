class Solution:
    def plusOne(self, digits):
        carry_one = True
        for i in range(len(digits) - 1, -1, -1):
            cur_digit = digits[i]
            cur_digit += 1 if carry_one else 0
            carry_one = cur_digit == 10
            digits[i] = 0 if carry_one else cur_digit
            if not carry_one:
                break
        if carry_one:
            digits.insert(0, 1)
        return digits


s = Solution()
print(s.plusOne([9, 9, 9]))
