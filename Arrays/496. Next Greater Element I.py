class Solution:
    def nextGreaterElement(self, x: List[int], y: List[int]) -> List[int]:
        a=[]
        for i in range(len(x)):
            p=-1
            for j in range(y.index(x[i]),len(y)):
                if y[j]>x[i]:
                    p=y[j]
                    break
            a.append(p)
        return a