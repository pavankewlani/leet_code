class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = []
        b = {")": "(", "}": "{", "]": "["}
        
        for c in s:
            if c in b:
                if not a:
                    return False
                if a.pop() != b[c]:
                    return False
            else:
                a.append(c)
                
        if len(a) == 0:
            return True
        else:
            return False