class Solution:
    def checkValid(self, m: List[List[int]]) -> bool:
        n=[i for i in range(1,len(m)+1)]
        k=[]
        for i in range(len(m)):
            if n!=sorted(m[i]):

                return False
            for j in range(len(m)):
                k.append(m[j][i])
            if n!=sorted(k):
            
                return False
            k.clear()
        return True