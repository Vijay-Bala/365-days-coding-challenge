class Solution:
    def maximumWealth(self,x: List[List[int]]) -> int:
        m=0
        for i in range(len(x)):
            t=sum(x[i])
            if t>m:
                m=t
        return m