class Solution:
    def sumZero(self, n: int) -> List[int]:
        x=[] if n%2==0 else [0]
        n=n if n%2==0 else n-1
        for i in range(n//2):
            x+=[i+1,-(i+1)]
        return x