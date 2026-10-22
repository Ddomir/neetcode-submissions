class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        for a in s:
            if a not in sMap:
                sMap[a] = 1
            else:
                sMap[a] += 1
        
        tMap = {}
        for a in t:
            if a not in tMap:
                tMap[a] = 1
            else:
                tMap[a] += 1

        if sMap == tMap:
            return True
        return False