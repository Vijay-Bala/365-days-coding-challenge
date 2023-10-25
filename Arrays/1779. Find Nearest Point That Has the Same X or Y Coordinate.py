class Solution:
    def nearestValidPoint(self, x: int, y: int, a: List[List[int]]) -> int:
        b=[]
        for i in a:
            if i in b or (i[0]!=x and i[1]!=y):
                continue
            b.append(i)
        if len(b)==0:
            return -1
        d=abs(x-b[0][0])+abs(y-b[0][1])
        t=b[0]
        for i in range(1,len(b)):
            if d>(abs(x-b[i][0])+abs(y-b[i][1])):
                t=b[i]
                d=(abs(x-b[i][0])+abs(y-b[i][1]))
        return a.index(t)