class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i in range(len(nums)):
            if nums[i] in check.keys():
                return [i,check[nums[i]]]
            check[target-nums[i]]=i