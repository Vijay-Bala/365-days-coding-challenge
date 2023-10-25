class Solution:
    def furthestDistanceFromOrigin(self, x: str) -> int:
        return x.count('_')+abs(x.count('R')-x.count('L'))