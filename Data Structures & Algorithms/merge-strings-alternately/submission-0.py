class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = []
        a = 0
        b = 0
        
        while(a < len(word1) or b < len(word2)):
            if(a < len(word1)):
                i = word1[a]
                res.append(i)
                a+=1
                
            if(b < len(word2)):
                j = word2[b]
                res.append(j)
                b+=1
        return "".join(res)