class Solution:
    def findGCD(self, x: List[int]) -> int:
        a=min(x)
        b=max(x)
        t=a
        while t!=0:
            if a%t==0 and b%t==0:
                return t
            t-=1