class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) %2 != 0:
            return False
        mapping = {")": "(", "}": "{", "]": "["}
        stack:List[str] = []
        for char in s :
            if char in mapping:
                top  = stack.pop() if stack else "#"
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack