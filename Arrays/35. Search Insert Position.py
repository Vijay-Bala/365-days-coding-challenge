class Solution:
    def searchInsert(self, a: List[int], x: int) -> int:
        if x in a:
            return a.index(x)
        i=0
        j=len(a)-1
        while a[i]<x and a[j]>x:
            i+=1
            j-=1
        if a[i]>x:
            return i
        if a[j]<x:
            return j+1