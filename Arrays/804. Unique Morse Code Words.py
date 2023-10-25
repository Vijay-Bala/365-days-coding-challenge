class Solution:
    def uniqueMorseRepresentations(self, x: List[str]) -> int:
        return len(set(["".join([[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."][ord(i)-97] for i in j]) for j in x]))