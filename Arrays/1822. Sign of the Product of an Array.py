class Solution:
    def arraySign(self, x: List[int]) -> int:
        c=0
        for i in x:
            if i==0:
                return 0
            if i<0:
                if c==0:
                    c=1
                else:
                    c=0
        if c==0:
            return 1
        return -1