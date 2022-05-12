class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightIndex = -1
        for i in range(len(arr)-1, -1 , -1):
            newMax = max(arr[i], rightIndex)
            arr[i] = rightIndex
            rightIndex = newMax
        return arr