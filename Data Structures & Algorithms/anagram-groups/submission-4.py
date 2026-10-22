class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        comboIndicies = defaultdict(list)
        for s in strs:
            sKey = "".join(sorted(s))
            comboIndicies[sKey].append(s)
        return list(comboIndicies.values())