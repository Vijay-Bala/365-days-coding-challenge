class Solution:
    def islandPerimeter(self, a: List[List[int]]) -> int:
        s=0
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j]==1:
                    s+=4
                    if i!=0:
                        if a[i-1][j]==1:
                            s-=1
                    if i<len(a)-1:
                        if a[i+1][j]==1:
                            s-=1
                    if j<len(a[i])-1:
                        if a[i][j+1]==1:
                            s-=1
                    if j!=0:
                        if a[i][j-1]==1:
                            s-=1
        return s