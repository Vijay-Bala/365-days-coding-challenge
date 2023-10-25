class Solution:
    def isGood(self, x: List[int]) -> bool:
        x.sort()
        return x==list(range(1,x[-1]))+[x[-1]]*2