class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaHash = defaultdict(list) # list of letters -> list of words
        
        for s in strs:
            ss = tuple(sorted(s)) # Hash can't have mutable key
            anaHash[ss].append(s)
        
        return list(anaHash.values()) # List of lists
        
