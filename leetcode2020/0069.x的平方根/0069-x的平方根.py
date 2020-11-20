class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        guess=1
        while 1:
            guess=(guess+x/guess)/2
            if abs(pow(guess,2)-x)<0.001:
                break
        res=int(guess)
        return res