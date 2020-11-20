class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result=roman[s[-1]]
        for i in range(len(s)-2,-1,-1):
            pre=roman[s[i+1]]
            cur=roman[s[i]]
            if cur<pre:
                result-=cur
            else:
                result+=cur
        return result