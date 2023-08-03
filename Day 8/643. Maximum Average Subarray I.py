class Solution:
    def findMaxAverage(self, x: List[int], k: int) -> float:
        s=t=sum(x[:k])
        for i in range(k,len(x)): s+=x[i]-x[i-k];t=max(t,s)
        return t/k
