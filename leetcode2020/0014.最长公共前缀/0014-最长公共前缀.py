class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:
            return ''
        prefix=strs[0]
        for i in range(1,len(strs)):
            if not prefix:
               return ''
            else:
               while prefix not in strs[i][:len(prefix)] and len(prefix)>0:
                   prefix=prefix[:len(prefix)-1]
        return prefix