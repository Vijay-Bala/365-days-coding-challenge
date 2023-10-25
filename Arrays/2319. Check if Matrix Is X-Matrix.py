class Solution:
    def checkXMatrix(self, x: List[List[int]]) -> bool:
        for i in range(len(x)):
            for j in range(len(x)):
                if (i==j or i+j==len(x)-1) and x[i][j]==0:
                    return False
                if j!=i and i+j!=len(x)-1 and x[i][j]!=0:
                    return False
        return True