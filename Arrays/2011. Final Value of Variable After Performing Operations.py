class Solution:
    def finalValueAfterOperations(self, a: List[str]) -> int:
        x=0
        for i in a:
            if "-" in i:
                x-=1
            else:
                x+=1
        return x