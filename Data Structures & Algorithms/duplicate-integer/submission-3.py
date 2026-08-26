class Solution:
    def hasDuplicate(self, nums):
        sett = set()
        for num in nums:
            if num in sett:
                return True
            sett.add(num)
        return False      
        