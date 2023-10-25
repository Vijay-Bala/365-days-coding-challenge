class Solution:
    def maxOperations(self, x: List[int], k: int) -> int:
        y={}
        c=0
        for i in x:
            if i in y: y[i]+=1
            else: y[i]=1
        for i in y:
            if k-i in y:
                if k==2*i:
                    c+=y[i]//2
                else:
                    t=min(y[k-i],y[i])
                    y[i]-=t
                    y[k-i]-=t
                    c+=t
        return c