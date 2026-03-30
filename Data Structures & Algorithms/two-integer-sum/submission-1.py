class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums1 = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in nums1:
                return [nums1[diff], i]
            nums1[n] = i
        return