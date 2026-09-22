class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix      # מכפלת כל האיברים משמאל ל-i
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix     # מכפיל במכפלת כל האיברים מימין ל-i
            suffix *= nums[i]

        return res