class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x<0):
            return False
        else:
            z=x
            temp=0
            while(x>0):
                tep=x%10
                temp=temp*10+tep
                x=x//10
            if(temp==z):
                return True
            else:
                return False
        