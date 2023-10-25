class Solution:
    def change(self, y: int, c: List[int]) -> int:
        x=[0]*(y+1)
        x[0]=1
        for i in c:
            for j in range(i,y+1):
                x[j]+=x[j-i]
        return x[y]