class Solution:
    def productExceptSelf(self, x: List[int]) -> List[int]:
        s=1
        for i in x:
            s*=i
        y=[]
        for i in range(len(x)):
            if x[i]==0:
                t=1
                for j in range(len(x)):
                    if i==j: continue
                    t*=x[j]
                y.append(t)
            else:
                y.append(s//x[i])
        return y