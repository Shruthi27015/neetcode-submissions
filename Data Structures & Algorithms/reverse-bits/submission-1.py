class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:]
        binary = binary.zfill(32)
        r = binary[::-1]
        return int(r, 2)