class Solution:
    def countKDifference(self, x: List[int], k: int) -> int:
        c=0
        for i in range(len(x)-1):
            for j in range(i+1,len(x)):
                if abs(x[i]-x[j])==k:
                    c+=1
        return c