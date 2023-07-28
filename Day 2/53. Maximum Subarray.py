class Solution:
    def maxSubArray(self, x: List[int]) -> int:
        s=t=x[0]
        for i in x[1:]:
            t=max(i,t+i)
            s=max(s,t)
        return s
