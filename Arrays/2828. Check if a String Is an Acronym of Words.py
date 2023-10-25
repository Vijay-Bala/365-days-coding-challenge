class Solution:
    def isAcronym(self, x: List[str], s: str) -> bool:
        return s=="".join([i[0] for i in x])