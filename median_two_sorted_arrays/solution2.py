from sys import maxsize
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        if (n1 < n2):
            return (self.findMedianSortedArrays(nums2, nums1))
        
        lo = 0
        hi = n2 * 2;
        while (lo <= hi):
            mid2 = (lo + hi) / 2
            mid1 = n1 + n2 - mid2
            
            if (mid1 == 0):
                L1 = -maxsize-1
            else:
                L1 = nums1[(mid1-1)/2]
            if (mid2 == 0):
                L2 =  -maxsize-1
            else: 
                L2 = nums2[(mid2-1)/2]
            
            if (mid1 == n1 * 2):
                R1 = maxsize
            else:
                R1 = nums1[(mid1)/2]
            
            if (mid2 == n2 * 2):
                R2 = maxsize
            else:
                R2 = nums2[(mid2)/2]
            
            if (L1 > R2):
                lo = mid2 + 1
            elif (L2 > R1):
                hi = mid2 - 1
            else:
                return (max(L1,L2) + min(R1, R2)) / 2
        return -1