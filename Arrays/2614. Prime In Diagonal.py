class Solution:
    def diagonalPrime(self, x: List[List[int]]) -> int:
        def fun(y):
            if y<=1:
                return False
            for i in range(2,int(y**0.5)+1):
                if y%i==0:
                    return False
            return True
        z=0
        n=len(x)
        for i in range(n):
            if fun(x[i][i]):
                z=max(z,x[i][i])
            if fun(x[i][n-i-1]):
                z=max(z,x[i][n-i-1])
        return z