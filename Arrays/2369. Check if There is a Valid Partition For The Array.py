class Solution:
    def validPartition(self, x: List[int]) -> bool:
        if len(x)==1: return False 
        y=[True,False,x[0]==x[1] if len(x)>1 else False] 
        for i in range(2,len(x)): 
            z=(x[i]==x[i-1] and y[1]) or (x[i]==x[i-1]==x[i-2] and y[0]) or (x[i]-x[i-1]==1 and x[i-1]-x[i-2]==1 and y[0])
            y[0],y[1],y[2]=y[1],y[2],z 
        return y[2]