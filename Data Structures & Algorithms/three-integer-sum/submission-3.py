class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        seen_i = set()
        
        for i in range(len(nums)):
            if nums[i] in seen_i:
                continue
            seen_i.add(nums[i])
            complements = set()

            for j in range(i + 1, len(nums)):
                complement = -nums[i] - nums[j]
                if complement in complements:
                    res.add(tuple(sorted((nums[i], nums[j], complement))))
                complements.add(nums[j])
        return [list(triplet) for triplet in res]