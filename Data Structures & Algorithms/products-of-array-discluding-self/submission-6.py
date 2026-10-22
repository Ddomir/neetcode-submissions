class Solution:
    def prefixArr(self, nums):
        arr = []
        totProd = 1
        for num in nums:
            totProd *= num
            arr.append(totProd)
        print(arr)
        return arr
    
    def postfixArr(self, nums):
        arr = [0] * len(nums)
        totProd = 1
        for i in range(len(nums) - 1, -1, -1):
            totProd *= nums[i]
            arr[i] = totProd
        print(arr)
        return arr

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pre = self.prefixArr(nums)
        post = self.postfixArr(nums)
        
        res[0] = post[1]
        res[n - 1] = pre[n - 2]

        if n > 2:
            for i in range(1, len(nums) - 1):
                res[i] = pre[i - 1] * post[i + 1]
        
        return res

