class Solution:
    def zeroFilledSubarray(self, x: List[int]) -> int:
        a=0
        t=0
        for i in range(len(x)):
            if x[i]==0:
                t+=1
            if x[i]!=0 or i==len(x)-1:
                a+=(t*(t+1))//2
                t=0
        return a