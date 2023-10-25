class Solution:
    def oddCells(self, m: int, n: int, x: List[List[int]]) -> int:
        y=[[0]*n for i in range(m)]
        for i in x:
            r=i[0]
            c=i[1]
            for j in range(n):
                y[r][j]+=1
            for k in range(m):
                y[k][c]+=1
        c=0
        for i in y:
            for j in i:
                if j%2!=0: c+=1
        return c