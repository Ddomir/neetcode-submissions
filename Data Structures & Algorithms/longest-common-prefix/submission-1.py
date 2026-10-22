class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        pre = ""

        for i, c in enumerate(strs[0]):
            for strn in strs:
                if i > (len(strn) - 1) or strn[i] != c:
                    return pre
                
            pre += c
        return pre