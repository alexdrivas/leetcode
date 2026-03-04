class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        # words must have equal length and contain the same set of letters
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False

        dict1 = {}
        dict2 = {}

        # Frewuency of each occurance 
        for c in word1:
            dict1[c] = dict1.get(c,0) + 1
        for c in word2: 
            dict2[c] = dict2.get(c,0) + 1
        
        # to do Op2, we must have the samenumber of frequencies for differnt letters, we can compare sorted lists. 
        d1 = list(dict1.values())
        d2 = list(dict2.values())
        d1.sort()
        d2.sort()
        return d1 == d2