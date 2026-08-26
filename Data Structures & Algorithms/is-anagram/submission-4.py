class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        
        if len(s) != len(t):
            return False
        
        for letter in range(len(s)):
            count[s[letter]] = count.get(s[letter], 0) + 1
            count[t[letter]] = count.get(t[letter], 0) - 1

        for value in count.values():
            if value != 0:
                return False
        
        return True