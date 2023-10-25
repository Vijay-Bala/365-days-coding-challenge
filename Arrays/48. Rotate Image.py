class Solution:
    def rotate(self, x: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # for i in range(len(x)):
        #     for j in range(i,len(x)):
        #         x[i][j],x[j][i]=x[j][i],x[i][j]
        y=[list(i) for i in zip(*x)]
        for i in range(len(y)):
            y[i]=y[i][::-1]
        print(y)
        x[:]=y[:]