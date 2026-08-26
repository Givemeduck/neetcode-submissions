class Solution:
    def twoSum(self, nums, target):
        sett = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in sett:
                return [sett[complement], i]
            sett[nums[i]] = i        
        