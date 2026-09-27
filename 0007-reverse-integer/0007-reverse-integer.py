class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        sign = -1 if x < 0 else 1
        z = abs(x)
        temp = 0
        
        while z > 0:
            tep = z % 10
            if temp > (INT_MAX - tep) // 10:
                return 0
            temp = temp * 10 + tep
            z = z // 10
        return sign * temp