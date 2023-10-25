class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        res = []
        for i in range(len(nums)):
            if target == nums[i]:
                return i
        
        for i in range(len(nums)):
            if target > nums[i]:
                res.append(nums[i])
        return len(res)    
        
        
