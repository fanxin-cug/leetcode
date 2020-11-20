import math
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y=str(x)
        if (x<0):
            a=y[1:] 
            b=a[::-1]
            c='-'+b
        else:
            c=y[::-1]
        res=int(c)
        if abs(res)>pow(2,31):
            return 0
        else:
            return res