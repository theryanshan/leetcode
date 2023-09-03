# shift each bit to the rightmost position and extract it
# then shift the bit to the 31 - i position and add it to the result


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += bit << (31 - i)
        return res
