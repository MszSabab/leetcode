class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        temp_dict={}
        uniques= []
        new_set = set()

        res = math.floor(len(nums)/3)

        for val in nums :
            if val in temp_dict:
                temp_dict[val]= temp_dict[val]+1

            else:
                temp_dict[val] = 1

            if temp_dict.get(val) > res :
                new_set.add(val)
        return list(new_set)