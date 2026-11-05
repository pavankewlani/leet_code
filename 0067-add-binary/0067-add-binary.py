class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum=int(a,2)+int(b,2)
        binary_8bit=format(sum,'b')
        return binary_8bit