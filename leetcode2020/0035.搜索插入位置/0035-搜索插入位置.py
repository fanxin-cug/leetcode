class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums==[]:
            return 0
        if target<nums[0]:
            return 0
        if target>nums[len(nums)-1]:
            return len(nums)
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            if target>nums[i] and target<nums[i+1]:
                return i+1