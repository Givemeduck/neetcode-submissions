class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" #encoding our strings into a single string
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
            #append the encoded string s by taking the length of the string (although the length is an  int, we're transforming it into a string). Then we're adding a delimiter to show that the int isn't part of the string
            #Looks like this: 4#bugs
    def decode(self, s: str) -> List[str]:
        res, i = [], 0 #the decoder result will be a list of strings
                    #'i' is the pointer that tells us which position we're at in the input string

        while i < len(s):
            j = i
            while s[j] != "#": #so while j hasn't reached the '#' symbol yet, it will keep counting
                                 #the strings till it has reached it
                j += 1
            length = int(s[i:j]) #the length of the string will be from index i all the way to index j
                                   #but it doesn't include index j as j will be the '#'
            res.append(s[j + 1 : j + 1 + length])
            #we want to find the length of the string after the '#' so we do
            #j + 1 all the way to the end of the string
            i = j + 1 + length #j + 1 + length is the beginning of the next string or the end of it
        return res

            