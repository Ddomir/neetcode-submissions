class Solution:
    def firstMissingPositive(self, a: List[int]) -> int:
        # Convert negatives to 0
        for i in range(len(a)):
            if a[i] < 0:
                a[i] = 0

        for i in range(len(a)):
            val = abs(a[i])
            if 1 <= val <= len(a):
                if a[val - 1] > 0:
                    a[val - 1] *= -1
                elif a[val - 1] == 0:
                    a[val - 1] = -1 * (len(a) + 1)

        for i in range(1, len(a) + 1):
            if a[i - 1] >= 0:
                return i

        return len(a) + 1