class Solution:
    def findRotation(self, x: List[List[int]], y: List[List[int]]) -> bool:
        for p in range(4):
            for i in range(len(x)):
                for j in range(i,len(x)):
                    x[i][j],x[j][i]=x[j][i],x[i][j]
            for i in range(len(x)):
                x[i]=x[i][::-1]
            if x==y:
                return True
        return False