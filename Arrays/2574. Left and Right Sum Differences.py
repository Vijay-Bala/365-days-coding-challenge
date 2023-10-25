class Solution:
    def leftRigthDifference(self, x: List[int]) -> List[int]:
        y=[0]
        z=[0]
        s=x[0]
        for i in range(1,len(x)):
            y.append(s)
            s+=x[i]
        s=x[-1]
        for i in range(len(x)-2,-1,-1):
            z.append(s)
            s+=x[i]
        z=z[::-1]
        for i in range(len(x)):
            x[i]=y[i]-z[i]
            if x[i]<0:
                x[i]*=-1
        return x