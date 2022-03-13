class Solution(object):
    def removeElement(self, nums, val):

        r = nums.count(val)
        for n in range(0, r):
            nums.remove(val)
        return len(nums)