class Solution:
    def numberOfBeams(self, x: List[str]) -> int:
        n="0"*len(x[0])
        while n in x: x.remove(n)
        s=0
        for i in range(len(x)-1):
            s+=x[i].count("1")*x[i+1].count("1")
        return s