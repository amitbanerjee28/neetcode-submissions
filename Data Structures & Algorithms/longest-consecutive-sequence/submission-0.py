class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        ls = 0
        for num in num_set:
            # current_num =0
            # current_streak=0
            if (num-1) not in num_set:
                current_num = num
                current_streak = 1
                while (current_num +1) in num_set:
                    current_num +=1
                    current_streak +=1
                ls = max(ls,current_streak)
        return ls 