class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnum = set(nums)
        if (len(setnum) == 1):
            longest = 1
        else:
            longest = 0
        for i in setnum:
            consecutive = 1
            q = i+1
            p = i-1
            while q in setnum:
                consecutive+=1
                q = q+1
            while p in setnum:
                consecutive+=1
                p = p-1
            if (consecutive > longest):
                longest = consecutive
        return longest