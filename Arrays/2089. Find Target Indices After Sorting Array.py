class Solution:
    def targetIndices(self, x: List[int], a: int) -> List[int]:
        l=[]
        if a in x:
            x.sort()
            n=x.count(a)
            p=x.index(a)
            while n>0:
                l.append(p)
                p+=1
                n-=1
        return l