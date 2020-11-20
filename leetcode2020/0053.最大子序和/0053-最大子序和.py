class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum=curSum=nums[0]
        for i in nums[1:]:
            curSum=max(i,curSum+i)
            maxSum=max(curSum,maxSum)
        return maxSum