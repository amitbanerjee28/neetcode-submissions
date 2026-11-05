class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer=[0]*n
        stack:List[int] = []
        for cd,ct in enumerate(temperatures):
            while stack and ct > temperatures[stack[-1]]:
                pd = stack.pop()
                answer[pd] = cd - pd
            stack.append(cd)
        return answer