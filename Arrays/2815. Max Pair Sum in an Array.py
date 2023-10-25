class Solution:
    def maxSum(self, x: List[int]) -> int:
        x=[list(str(i)) for i in x]
        # y=[i[0] for i in x]
        z={}
        for i in x:
            if max(i) not in z: z[max(i)]=1
            else: z[max(i)]+=1
        t=[]
        for i in z:
            if z[i]==1: t.append(i)
        for i in t:
            z.pop(i)
        if len(z)==0: return -1
        y=[]
        for i in z:
            t=[]
            for j in x:
                if i==max(j): t.append(int("".join(j)))
            y.append(t)
        for i in range(len(y)):
            t=max(y[i])
            y[i].remove(t)
            y[i]=t+max(y[i])
        return max(y)