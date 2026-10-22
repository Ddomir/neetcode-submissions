class Solution:
    def isPalindrome(self, s: str) -> bool:
        sChars = ""

        for l in s:
            if l.isalnum():
                sChars += l.lower()

        return sChars == sChars[::-1]
