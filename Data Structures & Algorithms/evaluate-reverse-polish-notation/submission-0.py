from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack:List[int] = []
        operations = {
            "*": lambda a,b:a*b,
            "-": lambda a,b:a-b,
            "+":lambda a,b:a+b,
            "/":lambda a,b:int(a/b),
        }
        for token in tokens:
            if token in operations:
                b =stack.pop()
                a = stack.pop()
                res = operations[token](a,b)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[0]