class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i, num in enumerate(nums):
            if target - num not in sums:
                sums[num] = i
            else:
                return [sums[target - num], i]
             