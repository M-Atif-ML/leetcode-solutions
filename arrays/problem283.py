class Solution(object):
    def moveZeroes(self, nums):
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[fast],nums[slow] = nums[slow],nums[fast]
                slow+=1
        
