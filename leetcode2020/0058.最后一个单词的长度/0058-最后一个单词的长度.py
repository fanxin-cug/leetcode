class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=='' or s.strip()=='':
            return 0
        col=s.split()
        return len(col[-1])