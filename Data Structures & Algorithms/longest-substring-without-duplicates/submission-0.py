class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 #beginning of sliding window
        longest = 0 #longest substring count
        sett = set()
        n = len(s)

        for r in range(n):
            while s[r] in sett: #while the letter's already in the set
                sett.remove(s[l])
                l += 1
            
            w = (r-l)+1
            longest = max(longest, w)
            sett.add(s[r])
        return longest