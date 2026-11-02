class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) ==0 or len(s) ==1:
            return True
        chars = list(s.replace(" ",""))
        j = len(chars)-1
        i = 0
        while i <= j:
            while i < j and not chars[i].isalnum():
                i += 1
            while i < j and not chars[j].isalnum():
                j -= 1
            if str(chars[i]).lower() != str(chars[j]).lower():
                return False
            i += 1
            j -= 1
        return True