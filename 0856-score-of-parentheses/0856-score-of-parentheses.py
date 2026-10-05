class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[0]
        for i in s:
            if(i=="("):
                stack.append(0)
            else:
                v=stack.pop()
                stack[-1] += max(2 * v, 1)
        return stack[0]