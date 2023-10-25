class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        x=[0,1]
        for i in range(1,n//2+1):
            x.append(x[i])
            x.append(x[i]+x[i+1])
        return max(x[:n+1])