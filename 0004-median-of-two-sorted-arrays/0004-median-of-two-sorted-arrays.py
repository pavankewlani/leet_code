class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()
        if(len(nums1)%2!=0):
            temp=(len(nums1)//2)
            return nums1[temp]

        else:
            temp=len(nums1)//2
            return ((nums1[temp]+nums1[temp-1])/2.0)