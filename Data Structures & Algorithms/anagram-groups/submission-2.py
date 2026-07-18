class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {} # key as sorted words and num
        for word in strs:
            key = "".join(sorted(word))
            if key not in words:
                words[key] = [word]
            else:
                words[key].append(word)
        return list(words.values())