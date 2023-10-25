class Solution:
    def shuffle(self, x: List[int], n: int) -> List[int]:
        y=[]
        for i in range(n):
            y.append(x[i])
            y.append(x[n+i])
        return y