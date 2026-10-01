class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        start, end = 0, 0
        
        for i in range(len(s)):
            left1, right1 = i, i
            while left1 >= 0 and right1 < len(s) and s[left1] == s[right1]:
                left1 -= 1
                right1 += 1
            len1 = right1 - left1 - 1
            
            left2, right2 = i, i + 1
            while left2 >= 0 and right2 < len(s) and s[left2] == s[right2]:
                left2 -= 1
                right2 += 1
            len2 = right2 - left2 - 1
            
            length = max(len1, len2)
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
                
        return s[start:end + 1]