class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        freq = {}
        for i in range(len(words)):
            freq[words[i]] = freq.get(words[i], 0) + 1

        sorted_list = sorted(freq.items(), key = lambda item: (-item[1], item[0])) 
        # creates list of tuples ex. [('i', 2), ('love', 2), ('coding', 1), ('leetcode', 1)]
        
        string_list = []
        for word,count in sorted_list[:k]:
            string_list.append(word) 
        return string_list