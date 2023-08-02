class Solution:
    def divide(self, x: int, y: int) -> int:
        s=-1 if (x>=0 and y<0) or (x<0 and y>=0) else 1
        x=abs(x)
        y=abs(y)
        r=len(range(0,x-y+1,y))
        if s==-1:
            r=-r
        a=-(2**31)
        b=2**31 - 1
        r=min(max(r,a),b)
        return r
