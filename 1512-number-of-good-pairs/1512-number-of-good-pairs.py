#need to optimize
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        uniques=[]
        temp_dict={}

        for i in range(len(nums)) :
            if nums[i] in uniques:
                temp_dict[nums[i]]= temp_dict[nums[i]]+1
            else:
                uniques.append(nums[i])
                temp_dict[nums[i]] = 1

        filtered_dict={}
        for k, v in temp_dict.items():
            if v > 1:
                filtered_dict[k]=v

        ans = 0
        for _,f in filtered_dict.items():
            ans=((f-1)*f/2)+ans
        return int(ans)