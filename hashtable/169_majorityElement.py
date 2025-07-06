class Solution(object):
    def majorityElement(self, nums):
        count = {}

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        ans = 0
        max_ = -9999
        for i, j in count.items():
            if j > max_:
                max_ = j
                ans = i
        return ans
