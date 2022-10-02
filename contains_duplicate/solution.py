class Solution(object):
    def containsDuplicate(self, nums):
        nums2 = set(nums)
        if len(nums2) != len(nums):
            return True
        return False
