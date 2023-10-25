class Solution:
    def projectionArea(self, x: List[List[int]]) -> int:
        s=len(x)*len(x[0])
        y=list(zip(*x))
        for i in x: s-=i.count(0)
        y=[list(y[i]) for i in range(len(y))]
        for i in x: s+=max(i)
        for i in y: s+=max(i)
        return s