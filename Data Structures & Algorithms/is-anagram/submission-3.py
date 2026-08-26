class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1 #appends the letters to hash set
            count[t[i]] = count.get(t[i], 0) - 1 #takes off letter from hash set
        

        for value in count.values():
            if value != 0:
                return False

        return True