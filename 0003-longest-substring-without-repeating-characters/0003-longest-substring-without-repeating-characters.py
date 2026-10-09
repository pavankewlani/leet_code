class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = ""
        max_len = 0
        
        for i in s:
            if i in res:
                res = res[res.index(i) + 1:]
            res += i
            if len(res) > max_len:
                max_len = len(res)
                
        return max_len