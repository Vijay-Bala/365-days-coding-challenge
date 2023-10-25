class Solution:
    def uniquePathsWithObstacles(self, x: List[List[int]]) -> int:              
        m,n=len(x),len(x[0])        
        y=[[0]*(n+1) for i in range(m+1)]        
        y[0][1]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if not x[i-1][j-1]:
                    y[i][j]=y[i-1][j]+y[i][j-1]
        return y[-1][-1]