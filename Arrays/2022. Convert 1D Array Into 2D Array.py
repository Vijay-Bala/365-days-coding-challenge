class Solution:
    def construct2DArray(self, x: List[int], m: int, n: int) -> List[List[int]]:
        if len(x)!=m*n:
            return []
        p=0
        z=[]
        for i in range(m):
            z.append([])
        for i in range(m):
            for j in range(n):
                z[i].append(x[p])
                p+=1
        return z