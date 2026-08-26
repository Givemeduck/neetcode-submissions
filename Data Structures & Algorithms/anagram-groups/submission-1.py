from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list) #for each key we're adding to map, we want default value to be empty list
        result = []

        #go through each of the words to check if they're an anagram and add them to anagram_map
        for s in strs:
            #sort the strings in alphabetical order so all of the anagrams will be in the same combo of numbers
            #ex: ate, eat, and tea will be all sorted as "a, e, t"
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)
        for value in anagram_map.values(): #gives us a list of the values in anagram_map
            result.append(value)
        
        return result