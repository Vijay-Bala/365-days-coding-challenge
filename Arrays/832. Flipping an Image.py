class Solution:
    def flipAndInvertImage(self, x: List[List[int]]) -> List[List[int]]:
        for i in range(len(x)):
            for j in range(len(x[i])):
                if x[i][j]==1:
                    x[i][j]=0
                else:
                    x[i][j]=1
            x[i]=x[i][::-1]
        return x