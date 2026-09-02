class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for word in strs:
            sort = "".join(sorted(word))
            if sort not in words:
                words[sort] = []
                words[sort].append(word)
            else:
                words[sort].append(word)
        return list(words.values())
                