class Solution:
    def increasingTriplet(self, x: List[int]) -> bool:
        a=b=float('inf')
        for i in x:
            if i<=a: a=i
            elif i<=b: b=i
            else: return True
        return False