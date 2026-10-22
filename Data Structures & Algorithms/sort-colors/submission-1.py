class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, red, white, blue = 0, 0, 0, 0
        for n in nums:
            if n == 0:
                red += 1
            elif n == 1:
                white += 1
            else:
                blue += 1
        
        for r in range(red):
            nums[i] = 0
            i += 1

        for w in range(white):
            nums[i] = 1
            i += 1
        
        for b in range(blue):
            nums[i] = 2
            i += 1
        """
        Do not return anything, modify nums in-place instead.
        """
        