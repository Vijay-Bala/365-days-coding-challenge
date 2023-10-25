class Solution:
    def numUniqueEmails(self, x: List[str]) -> int:
        y=set()
        for i in x:
            j,k=i.split('@')
            t=""
            for c in j:
                if c==".": continue
                elif c=="+": break
                else: t+=c
            y.add(t+"@"+k)
        return len(y)