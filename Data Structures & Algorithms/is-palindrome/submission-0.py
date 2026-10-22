class Solution:
    def isPalindrome(self, s: str) -> bool:
        sChars = ""

        for l in s:
            if l.isalpha() or l.isdigit():
                sChars += l.lower()

        for i in range(len(sChars)//2):
            if sChars[i] != sChars[len(sChars) - 1 - i]:
                return False
        
        return True
