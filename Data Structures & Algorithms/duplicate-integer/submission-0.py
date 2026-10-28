class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        r = []
        for i in range(0,len(nums)):
            if nums[i] in r:
                return True
            else:
                r.append(nums[i])
        return False
        