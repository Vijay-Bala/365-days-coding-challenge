class Solution:
    def nthUglyNumber(self, n: int) -> int:
        x=[1 if i==0 else 0 for i in range(n)]
        a=b=c=0
        for i in range(1,n):
            x[i]=min(x[a]*2,x[b]*3,x[c]*5)
            if(x[i]==x[a]*2): a+=1
            if(x[i]==x[b]*3): b+=1
            if(x[i]==x[c]*5): c+=1
        return x[n-1]