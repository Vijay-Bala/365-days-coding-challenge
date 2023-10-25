class Solution:
    def diagonalSum(self, x: List[List[int]]) -> int:
        s=0
        i=0
        j=len(x)
        while i<j:
            s+=x[i][i]
            s+=x[i][j-i-1]
            i+=1
        if j%2!=0:
            s-=x[j//2][j//2]
        return s