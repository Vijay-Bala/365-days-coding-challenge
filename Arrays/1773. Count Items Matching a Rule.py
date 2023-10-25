class Solution:
    def countMatches(self, x: List[List[str]], k: str, v: str) -> int:
        c=0
        if k=="type":
            p=0
        elif k=="color":
            p=1
        else:
            p=2
        for i in x:
            if i[p]==v:
                c+=1
        return c