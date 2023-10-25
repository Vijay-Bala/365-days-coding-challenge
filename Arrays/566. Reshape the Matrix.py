class Solution:
    def matrixReshape(self, x: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(x)
        n=len(x[0])
        if m*n!=r*c:
            return x
        z=[]
        r1=0
        c1=0
        for i in range(r):
            t=[]
            for j in range(c):
                if c1==n:
                    c1=0
                    r1+=1
                t.append(x[r1][c1])
                c1+=1
            z.append(t)
        return z