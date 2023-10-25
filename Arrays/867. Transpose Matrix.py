class Solution:
    def transpose(self, x: List[List[int]]) -> List[List[int]]:
        y=list(zip(*x))
        for i in range(len(y)):
            y[i]=list(y[i])
        return y