class Solution:
    def setZeroes(self, x: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        y=[1]*len(x)
        z=[1]*len(x[0])
        for i in range(len(x)):
            for j in range(len(x[0])):
                if x[i][j]==0: y[i]=0;z[j]=0
        for j in range(len(x[0])):
            if z[j]!=0: continue
            for i in range(len(x)):
                x[i][j]=0
        for i in range(len(x)):
            if y[i]!=0: continue
            for j in range(len(x[0])):
                x[i][j]=0