class Solution:
    def isToeplitzMatrix(self, x: List[List[int]]) -> bool:
        for i in range(len(x)-1):
            for j in range(len(x[i])-1):
                if x[i][j]!=x[i+1][j+1]:
                    return False
        return True