class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        if(len(nums) == 1 or len(nums) == 0):
            return False
        for i in range(len(nums)-1):
            if(nums[i] == nums[i+1]):
                return True
        return False        
            