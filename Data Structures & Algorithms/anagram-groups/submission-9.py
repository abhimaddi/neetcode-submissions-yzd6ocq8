class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for word in strs:
            temp = ''.join(sorted(word))
            if temp not in words:
                words[temp] = []
            words[temp].append(word)
        return list(words.values())