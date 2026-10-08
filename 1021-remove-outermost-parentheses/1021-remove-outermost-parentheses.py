class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=[]
        depth=0
        
        for char in s:
            if char == '(' :
                if depth > 0:
                    result.append(char)
                depth += 1
            else: # char == ')'
                depth -= 1
                if depth > 0:
                    result.append(char)
        return "".join(result)