class Solution:
    def removeElement(self, x: List[int], a: int) -> int:
        while(a in x):
            x.remove(a)
        return len(x)