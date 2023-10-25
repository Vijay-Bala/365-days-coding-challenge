class Solution:
    def average(self, x: List[int]) -> float:
        return((sum(x)-(max(x)+min(x)))/(len(x)-2))