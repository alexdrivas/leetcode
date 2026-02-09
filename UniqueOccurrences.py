class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        # create a dict containing value, occurrences
        # create a set of distinct values in the dict 
        # compare length of set and dict to determine if occurrences are unique

        my_dict = {}
        for i in arr:
            if i not in my_dict.keys():
                my_dict[i] = 1
            else:
                my_dict[i] += 1

        set1 = set(my_dict.values())
        return len(set1) == len(my_dict)