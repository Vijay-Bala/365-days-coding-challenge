class Solution:
    def arithmeticTriplets(self, x: List[int], y: int) -> int:
        c=0
        for i in x:
            if i+y in x and i+y*2 in x: c+=1
        return c