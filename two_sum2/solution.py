class Solution(object):
    def twoSum(self, nums, target):
        hash_table = {}
        for i in range(len(nums)):
            if nums[i] in hash_table:
                return [hash_table[nums[i]] + 1, i + 1]
            else:
                hash_table[target - nums[i]] = i