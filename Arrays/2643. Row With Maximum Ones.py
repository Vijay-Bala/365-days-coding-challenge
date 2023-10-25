class Solution:
    def rowAndMaximumOnes(self, x: List[List[int]]) -> List[int]:
        c=[i.count(1) for i in x]
        return [c.index(max(c)),max(c)]