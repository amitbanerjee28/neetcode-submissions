class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # seen: dict[int,int] = {}
        # for idx,num in enumerate(numbers):
        #     compliment= target -num
        #     if compliment in seen:
        #         return [seen[compliment],idx+1]
        #     seen[num] = idx + 1
        left = 0
        right = len(numbers) -1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left +1, right +1]
            if sum < target:
                left +=1 
            else:
                right -=1