class Solution:
    def minEatingSpeed(self, x: List[int], h: int) -> int:
        l=ceil(sum(x)/h) 
        r=max(x) 
        while l<r:
            m=(l+r)//2
            t=0
            for i in x:
                t+=ceil(i/m)
                if t>h:
                    break
            if t<=h:
                r=m
            else:
                l=m+1
        return r