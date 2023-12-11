class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        lenOfArr = len(arr)

        dct=dict()

        averValue =  int((lenOfArr) * (25 / 100))
        for v in arr:
            dct.update({
                v: dct.get(v, 0) + 1
            })
            if dct.get(v) > averValue:
                return v