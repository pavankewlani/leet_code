class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        if not s:
            return 0
            
        sign = 1
        start_index = 0
        if s[0] == '-':
            sign = -1
            start_index = 1
        elif s[0] == '+':
            start_index = 1
            
        result = 0
        has_digits = False
        for i in range(start_index, len(s)):
            char = s[i]
            code = ord(char)
            if code >= 48 and code <= 57:
                has_digits = True
                result = result * 10 + (code - 48)
            else:
                break
                
        if not has_digits:
            return 0
            
        result = result * sign
        
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
            
        return result