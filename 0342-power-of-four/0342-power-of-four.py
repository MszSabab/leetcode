import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        l =[]
        for i in range(16):
            x= pow(4,i)
            l.append(x)
        
        if n in l:
            return True
        else:
            return False    