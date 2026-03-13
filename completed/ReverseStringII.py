class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l, r = 0,k-1
        output = ""

        while l < len(s):
            # get reverse string slice
            reversed_chunk = s[l:r+1][::-1]#[l:r+1:-1]
            output += reversed_chunk

            # move l
            l += 2*k

            #get chunk s[r+1, l] 
            chunk = s[r+1: l]

            # add chunk 
            output += chunk 

            # move r 
            r = l + k -1
        return output   