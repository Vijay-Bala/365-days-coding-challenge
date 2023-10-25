class Solution:
    def triangularSum(self, x: List[int]) -> int:
        while len(x)!=1:
            t=[]
            for i in range(len(x)-1):
                t.append((x[i]+x[i+1])%10)
            x=t
        return x[0]