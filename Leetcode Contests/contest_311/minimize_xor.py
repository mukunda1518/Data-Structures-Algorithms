# Leetcode:https://leetcode.com/problems/minimize-xor/description/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        set_bits_count = bin(num2)[2:].count("1")
        bin_num1 = bin(num1)[2:]
        bin_num1 = "0" * (32 - len(bin_num1)) + bin_num1
        bin_num1 = [x for x in bin_num1]
        res = ["0"] * 32

        for i in range(32):
            if bin_num1[i] == "1":
                if set_bits_count:
                    set_bits_count -= 1
                    res[i] = "1"
                else:
                    break
        if not set_bits_count:
            return int("".join(res), 2)

        for i in range(31, -1, -1):
            if bin_num1[i] != "1":
                res[i] = "1"
                set_bits_count -= 1
            if not set_bits_count:
                break
        return int("".join(res), 2)
