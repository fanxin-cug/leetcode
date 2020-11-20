class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack)<2:
            if haystack==needle or needle=="":
                return 0
            else:
                return -1
        for i in range(len(haystack)): 
            if i+len(needle)<=len(haystack) and haystack[i:i+len(needle)]==needle:
                return i
        else:
            return -1