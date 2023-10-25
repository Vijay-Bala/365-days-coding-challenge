class Solution:
    def longestOnes(self, x: List[int], y: int) -> int:
      j=i=0
      for i in range(len(x)):
        if x[i]==0: y-=1
        if y<0:
          if x[j]==0: y+=1
          j+=1      
      return i-j+1