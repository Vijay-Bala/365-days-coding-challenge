class Solution:
    def maxSum(self, x: List[int], m: int, k: int) -> int:
        if len(x)<k or len(set(x))<m: return 0
        z=x[:k]
        s=0 if len(set(z))<m else sum(z)
        for i in range(len(x)-k):
            z.remove(x[i])
            z.append(x[i+k])
            if len(set(z))<m: continue
            s=max(s,sum(z))
        return s