class Solution(object):

    def twoSum(self, nums, target):
  
        
        self.nums = nums
        self.target = target
        lenght = len(nums)
        for i in range(lenght):
            for j in range(lenght):
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]
          
        return []
