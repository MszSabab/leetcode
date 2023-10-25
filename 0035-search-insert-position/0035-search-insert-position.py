
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums_lower = []
        for i in range(len(nums)):
            if target == nums[i]:
                return i
        for i in range(len(nums)):
            if target > nums[i]:
            # till it is less than, find that index and then return that value
                nums_lower.append(nums[i])
        return len(nums_lower)