class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        h = {}
        for i in s:
            y=''.join(sorted(i))
            if y not in h:
                h[y]=[i]
            else:
                h[y].append(i)
        x=[]
        for i in h.values():
            x.append(i)
        return x