class Solution:
    def minimizeMax(self, x: List[int], p: int) -> int:
        if p==0 or x==[]: return 0
        x.sort()
        l,r=0,x[-1]-x[0]
        while l<r:
            m,c,i=(l+r)//2,0,0
            while i<len(x)-1 and c<p:
                c,i=(c+1,i+2) if x[i+1]-x[i]<=m else (c,i+1)
            l,r=(l,m) if c>=p else (m+1,r)
        return l