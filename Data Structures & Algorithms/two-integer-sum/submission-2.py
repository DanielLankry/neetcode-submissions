class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, num in enumerate(nums):
            complete = target - num
            if complete in hash_map:
                return [hash_map[complete],i]
            hash_map[num] = i
        