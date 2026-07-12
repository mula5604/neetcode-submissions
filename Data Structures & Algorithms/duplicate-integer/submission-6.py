class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i,num in enumerate(nums):
            try:
                if num == nums[i+1]:
                    return True
            except IndexError:
                return False
        return False
