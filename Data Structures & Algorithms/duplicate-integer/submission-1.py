class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        r = set()
        for i in range(0,len(nums)):
            if nums[i] in r:
                return True
            else:
                r.add(nums[i])
        return False
        