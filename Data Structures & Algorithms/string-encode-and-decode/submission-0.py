class Solution:

    def encode(self, strs: List[str]) -> str:
         res = ""
         for s in strs:
            res += str(len(s))
            res += "@"
            res += s

         return res

    def decode(self, s: str) -> List[str]:
         res,i = [], 0

         while i < len(s):
             j = s.find("@",i)
             start = j + 1
             length = int(s[i:j])
             word = s[start: start + length]
             res.append(word)
             i = start + length

         return res




        
