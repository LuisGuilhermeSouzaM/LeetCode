class Solution(object):
    def longestConsecutive(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        longest, current_longest = 0 , min(1,len(nums))
        print(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]: 
                continue
            if nums[i + 1] - nums[i] == 1:
                current_longest += 1
            else: 
                longest, current_longest = max(current_longest,longest), 1
        return max(current_longest,longest)
    if __name__ == "__main__":
        nums = [0,3,7,2,5,8,4,6,0,1]
        print(longestConsecutive(nums))