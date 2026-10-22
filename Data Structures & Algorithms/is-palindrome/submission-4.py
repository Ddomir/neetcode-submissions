class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while True:
            if l >= len(s) or r <= 0:
                return True
                
            while not s[l].isalnum():
                if l >= r or l >= len(s):
                    return True
                l += 1
            
            while not s[r].isalnum():
                if l >= r or r <= 0:
                    return True
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

