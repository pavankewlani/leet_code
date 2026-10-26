class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) ^ (divisor < 0)

        a = dividend if dividend < 0 else -dividend
        b = divisor if divisor < 0 else -divisor

        quotient = 0

        while a <= b:
            temp_b = b
            multiple = 1
            while temp_b >= (INT_MIN >> 1) and a <= (temp_b << 1):
                temp_b <<= 1
                multiple <<= 1
            
            a -= temp_b
            quotient += multiple

        return -quotient if negative else quotient