class Solution:
    def decompressRLElist(self, x: List[int]) -> List[int]:
        y=[]
        for i in range(0,len(x),2):
            t=[x[i+1] for c in range(x[i])]
            y=y+t
        return y