class Solution(object):
    def removeDuplicates(self, nums):
        
        if nums:
            nums[:] = sorted(list(set(nums)))
        
