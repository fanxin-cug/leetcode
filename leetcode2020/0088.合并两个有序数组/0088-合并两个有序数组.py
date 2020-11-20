class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while len(nums1)!=m:
            nums1.pop()
        if m==0:
            for i in range(len(nums2)):
                nums1.append(nums2[i])
        else:
            if n!=0:
                i=j=0
                while j<n:
                    nums1.append(nums2[j])
                    if nums1[0]>=nums1[-1]:
                        temp=nums1[0]
                        nums1[0]=nums1[-1]
                        for k in range(1,len(nums1)-1):
                            nums1[len(nums1)-k]=nums1[len(nums1)-k-1]
                        nums1[1]=temp
                    else:
                        while i<len(nums1) and nums1[i]<nums1[-1]:
                            i+=1
                        if i!=len(nums1)-1:
                            temp=nums1[i]
                            nums1[i]=nums1[-1]
                            for k in range(len(nums1)-1,i,-1):
                                nums1[k]=nums1[k-1]
                            nums1[i+1]=temp
                    j+=1
        return