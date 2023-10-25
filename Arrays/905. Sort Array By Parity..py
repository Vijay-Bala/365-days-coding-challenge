class Solution:
    def sortArrayByParity(self, x: List[int]) -> List[int]:
        return [i for i in x if i%2==0]+[j for j in x if j&1]