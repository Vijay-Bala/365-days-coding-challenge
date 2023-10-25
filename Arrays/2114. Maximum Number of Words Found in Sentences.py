class Solution:
    def mostWordsFound(self, x: List[str]) -> int:
        m=0
        for i in range(len(x)):
            t=len(list(map(str,x[i].split(' '))))
            if t>m:
                m=t
        return m