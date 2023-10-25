class Solution:
    def smallerNumbersThanCurrent(self, x: List[int]) -> List[int]:
        y=sorted(x)
        return [y.index(i) for i in x]