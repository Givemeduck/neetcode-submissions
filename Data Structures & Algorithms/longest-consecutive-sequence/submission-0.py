class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums) #creating a set from the initial array
        
        longest = 0 #keep track of longest sequence

        for i in nums:
            #check if it's the start of a sequence
            if (i-1) not in sett:
                length = 0
                while (i + length) in sett:
                    length += 1
                longest = max(length, longest)
        return longest        
