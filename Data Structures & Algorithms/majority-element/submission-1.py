class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sett = {}

        for num in nums:
            sett[num] = sett.get(num, 0) + 1

        for num in sett:
            if sett[num] > len(nums) // 2:
                return num
