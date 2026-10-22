class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def swap(a, b, l):
            tmp = l[a]
            l[a] = l[b]
            l[b] = tmp

        for i in range(len(s)//2):
            swap(i, len(s) - 1 - i, s)
            
