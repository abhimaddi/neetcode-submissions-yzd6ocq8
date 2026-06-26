class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        seen_i = set()
        
        for i in range(len(nums)):
            # Skip duplicates for the first element to save time
            if nums[i] in seen_i:
                continue
            seen_i.add(nums[i])
            
            # Inner loop acts like standard Two Sum with a hash set
            complements = set()
            for j in range(i + 1, len(nums)):
                complement = -nums[i] - nums[j]
                if complement in complements:
                    # Store as a sorted tuple to easily handle duplicate triplets in the result set
                    res.add(tuple(sorted((nums[i], nums[j], complement))))
                complements.add(nums[j])
                
        return [list(triplet) for triplet in res]