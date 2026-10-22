class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anaGroups = defaultdict(list)

        for s in strs:
            anaGroups[tuple(sorted(s))].append(s)
        
        return list(anaGroups.values())