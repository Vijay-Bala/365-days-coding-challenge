class Solution:
    def countConsistentStrings(self, x: str, y: List[str]) -> int:
        z=[list(set(list(i))) for i in y]
        c=0
        for i in y:
            f=1
            for j in i:
                if j not in x:
                    f=0
                    break
            if f==1:
                c+=1
        return c