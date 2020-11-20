class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        y=list()
        for item in digits:
            x=str(item)
            y.append(x)
        res=''
        for i in range(len(y)):
            res+=y[i]
        res1=int(res)
        ans=res1+1
        ans1=str(ans)
        z=list()
        for i in range(len(ans1)):
            z.append(int(ans1[i]))
        return z   
