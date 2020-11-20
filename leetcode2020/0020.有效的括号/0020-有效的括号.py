class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        para=[None]
        par={')':'(',']':'[','}':'{'}
        for x in s:
            if x in par and par[x]==para[len(para)-1]:
               para.pop()
            else:
               para.append(x)
        return len(para)==1