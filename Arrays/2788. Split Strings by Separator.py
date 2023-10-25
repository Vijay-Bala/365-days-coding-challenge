class Solution:
    def splitWordsBySeparator(self, x: List[str], y: str) -> List[str]:
        z=[]
        for i in x: z.extend(list(map(str,i.split(y))))
        while "" in z: z.remove("")
        return z