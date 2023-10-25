class Solution:
    def canMakeArithmeticProgression(self, x: List[int]) -> bool:
        x.sort()
        if len(x)==1 or len(x)==2:
            return True
        i=0
        j=1
        while i<len(x) and j+1<len(x):
            if x[i]-x[j]!=x[j]-x[j+1]:
                return False
            i+=1
            j+=1
        return True