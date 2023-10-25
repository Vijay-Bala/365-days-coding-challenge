class Solution:
    def canPlaceFlowers(self, x: List[int], n: int) -> bool:
        if len(x)==1 and x[0]==0 and n==1:
            return True
        m=x.count(1)
        for i in range(len(x)-1):
            if i==0 and x[i]==0 and x[i+1]==0:
                x[i]=1
            elif i==len(x)-2 and x[i]==0 and x[i+1]==0:
                x[i+1]=1
            else:
                if x[i]==0 and x[i-1]==0 and x[i+1]==0:
                    x[i]=1
        if x.count(1)>=m+n:
            return True
        return False