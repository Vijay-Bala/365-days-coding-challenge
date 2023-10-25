from itertools import permutations as p
class Solution:
    def permute(self, x: List[int]) -> List[List[int]]:
        return p(x,len(x))