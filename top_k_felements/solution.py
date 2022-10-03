class Solution(object):
    def topKFrequent(self, nums, k):
        new_list = []
        mf = {}
        for i in range(len(nums)):
            if nums[i] in mf:
                mf[nums[i]] += 1
            else:
                mf[nums[i]] = 1
        a = [0] * (len(mf))
        j = 0
        for i in mf:
            a[j] = [i, mf[i]]
            j += 1
        a = sorted(a, key=lambda x: x[0], reverse=True)
        a = sorted(a, key=lambda x: x[1], reverse=True)
        for i in range(k):
            new_list.append(a[i][0])
        return new_list