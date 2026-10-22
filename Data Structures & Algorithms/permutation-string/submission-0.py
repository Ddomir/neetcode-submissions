from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1f = Counter(s1)
        s1l = len(s1)
        
        for i in range(len(s2) - s1l + 1):
            freq = Counter(s2[i:i+s1l])
            if s1f == freq:
                return True
        return False
