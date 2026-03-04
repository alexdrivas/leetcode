class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        my_list = s.split() 
        word = my_list.pop()
        return len(word)