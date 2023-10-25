class Solution:
    def search(self, x: List[int], a: int) -> int:
        if a in x:
            return x.index(a)
        return -1