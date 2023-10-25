class Solution:
    def separateDigits(self, x: List[int]) -> List[int]:
        z=[]
        for i in x:
            t=[]
            while i!=0:
                t.append(i%10)
                i//=10
            for i in t[::-1]:
                z.append(i)
        return z