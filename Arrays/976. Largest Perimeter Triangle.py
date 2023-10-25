class Solution:
    def largestPerimeter(self, x: List[int]) -> int:
        x=sorted(x)[::-1]
        for i in range(3,len(x)+1):
            if x[i-3]<x[i-2]+x[i-1]:
                return sum(x[i-3:i])
        return 0