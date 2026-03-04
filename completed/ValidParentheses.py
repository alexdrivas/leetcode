class Solution:
    def isValid(self, s: str) -> bool:

        # Create dict
        dic = {
            "(": ")", 
            "[": "]", 
            "{": "}"
        }

        stack = []

        for c in s:
            if c in dic:
                stack.append(c)
            else:
                if stack == [] or dic[stack.pop()] != c:
                    return False

        return True if stack == [] else False