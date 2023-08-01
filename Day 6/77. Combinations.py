from itertools import combinations as c
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return c(range(1,n+1),k)