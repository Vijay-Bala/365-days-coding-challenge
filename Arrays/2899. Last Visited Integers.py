class Solution:
    def lastVisitedIntegers(self, x: List[str]) -> List[int]:
        c=0
        z=[]
        for i in range(len(x)):
            y=[j for j in x[:i+1] if j!="prev"][::-1]
            if x[i]=="prev":
                c+=1
                z.append(int(y[c-1]) if c<=len(y) else -1)
            else: c=0
        return z