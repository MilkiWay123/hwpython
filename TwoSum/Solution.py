class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index = {}
        for i in range(len(nums)):
            index[nums[i]] = i
        for i in range(len(nums)):
            k = index.get(target - nums[i])
            if k is not None and k != i:
                return [i, k]
