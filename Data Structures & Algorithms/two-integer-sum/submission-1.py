class Solution:
    def twoSum(self, nums, target):
        num_set = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_set:
                return [num_set[complement], i]
            num_set[nums[i]] = i
        