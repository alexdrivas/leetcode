# 409. Longest Palindrome
class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        d = {}
        for char in s:
            d[char] = d.get(char,0) + 1
        
        length = 0
        bazooka = False

        if len(d) == 1:
            for value in d.values():
                return value
        
        for i in d: 
            length += ((d[i]//2) * 2)
            if d[i] % 2 == 1:
                bazooka = True
        
        if bazooka == True:
            print("FIRE")
            length += 1

        return length