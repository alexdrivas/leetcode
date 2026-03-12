class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mylist = list()
        max_length = 0
        length = 0


        for i in s:
            # if the char is not in set then progress
            if i not in mylist:
                mylist.append(i)
                length = len(mylist)

            else: 
                # determine length of set 
                length = len(mylist)
                max_length = max(max_length, length)

                # slice the list beyond the repeated element 
                index = mylist.index(i)
                mylist = mylist[index+1::]
                mylist.append(i)

        max_length = max(max_length, length)    
        return max_length