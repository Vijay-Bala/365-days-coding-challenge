class Solution:
    def decode(self, x: List[int], f: int) -> List[int]:
        y=[f]
        for i in x:
            y.append(y[-1]^i)
        return y