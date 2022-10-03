def productExceptSelf(nums):
    prefix = [1] * len(nums)
    suffix = [1] * len(nums)
    answer = [0] * len(nums)
    prefix[0] = 1
    suffix[len(nums) - 1] = 1
    for i in range(1, len(nums)):
        prefix[i] = prefix[i - 1] * nums[i - 1]
    for i in range(len(nums) - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]
    for i in range(len(nums)):
        answer[i] = prefix[i] * suffix[i]
    return answer, suffix, prefix
if __name__ == "__main__":
    nums = [1,2,3,4]
    print(productExceptSelf(nums))