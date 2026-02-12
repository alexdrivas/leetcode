class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ""
        s = sorted(strs)
        first = s[0]
        last = s[-1]
 
        for i in range(len(min(first, last))):
            if first[i] != last[i]:
                return res
            res += first[i]
        return res