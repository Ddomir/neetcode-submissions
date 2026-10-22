class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaHash = {} # list of letters -> list of words
        
        for s in strs:
            ss = tuple(sorted(s))
            if ss in anaHash:
                anaHash[ss].append(s)
            else:
                anaHash[ss] = [s]
        
        return list(anaHash.values())
        
