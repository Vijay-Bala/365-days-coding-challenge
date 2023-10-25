class Solution:
    def mostPoints(self, x: List[List[int]]) -> int:
        y=len(x)
        z=[0]*(y+1)
        for i in range(len(x)-1,-1,-1):
            a,b=x[i]
            t=i+b+1
            t=y if t>=y else t
            z[i]=max(z[i+1],a+z[t])
        return z[0]