class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1 or n==2:
            return n 
        x=[1,2]
        for i in range(n):
            y=x[i]+x[i+1]
            x.append(y)
            if len(x)==n:
                break
        return x[-1]