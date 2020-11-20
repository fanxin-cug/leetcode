class Solution:
    def countStr(s):
        count=0
        ans=''
        tmp=s[0]
        for i in range(len(s)):
            if s[i]==tmp:
                count+=1
            else:
                ans+=str(count)+tmp
                tmp=s[i]
                count=1
        ans+=str(count)+tmp
        return ans
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        x=list()
        x.append('1')
        for i in range(n):
            x.append(Solution.countStr(x[i]))
        return x[n-1]
           
