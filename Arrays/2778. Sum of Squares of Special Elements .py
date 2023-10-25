class Solution:
    def sumOfSquares(self, x: List[int]) -> int:
        return sum([x[i]**2 for i in range(len(x)) if len(x)%(i+1)==0])