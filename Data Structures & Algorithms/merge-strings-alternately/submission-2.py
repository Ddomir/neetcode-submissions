class Solution:
    def mergeAlternately(self, wordA: str, wordB: str) -> str:
        a = b = 0
        res = ''

        while a < len(wordA) and b < len(wordB):
            res += wordA[a] + wordB[b]
            a, b = a + 1, b + 1
        
        if a < len(wordA):
            #print("A: " + wordA[a:])
            res += wordA[a:]
        elif b < len(wordB):
            #print("B: " + wordB[b:])
            res += wordB[b:]
        
        return res