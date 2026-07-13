class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_sum = {}
        for i, num in enumerate(nums):
            complete = target - num
            if complete in hash_sum:
                return [hash_sum[complete], i]
            hash_sum[num] = i
        return []