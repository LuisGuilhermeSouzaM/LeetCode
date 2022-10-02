from sys import maxsize

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)
        half_size = total / 2

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        left = 0
        right = len(nums1) - 1

        while(True):
            i = (left + right)/2
            j = half_size - i - 2
            nums1_left = nums1[i] if i >= 0 else -maxsize - 1
            nums1_right = nums1[i + 1] if (i + 1) < len(nums1) else maxsize
            nums2_left = nums2[j] if j >= 0 else -maxsize - 1
            nums2_right = nums2[j + 1] if (j + 1) < len(nums2) else maxsize
            
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if total % 2:
                    return min(nums1_right, nums2_right)
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:
                right = i - 1
            else:
                left = i + 1