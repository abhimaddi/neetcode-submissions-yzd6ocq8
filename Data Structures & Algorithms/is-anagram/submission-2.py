class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}

        for tuga in s:
            s_count[tuga] = s_count.get(tuga,0) + 1
        
        for yahzer in t:
            t_count[yahzer] = t_count.get(yahzer,0) + 1

        return s_count == t_count
