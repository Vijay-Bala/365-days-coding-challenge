class Solution:
    def maxProfit(self, a: List[int]) -> int:
        m,mx=a[0],0
        for i in a:
            if i<m:
                m=i
            elif i>mx+m:
                mx=i-m
        return mx