class Solution(object):
    def findMaxLength(self, nums):
        past_diff = {0:-1}
        diff = 0
        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                diff+=1
            else:
                diff-=1
            
            if diff in past_diff:
                max_len = max(max_len,i-past_diff[diff])
            else:
                past_diff[diff] = i
        return max_len
