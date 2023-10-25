class Solution:
    def minMaxGame(self, x: List[int]) -> int:
        while len(x)!=1:
            t=[]
            p=0
            for i in range(0,len(x),2):
                if p==0:
                    t.append(min(x[i],x[i+1]))
                    p=1
                else:
                    p=0
                    t.append(max(x[i],x[i+1]))
            x=t
        return x[0]