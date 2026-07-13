class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
         res = defaultdict(int)
         ret = []

         for num in nums:
            res[num] += 1
        
         sorted_res = dict(sorted(res.items(), key=lambda item:item[1], reverse = True))
         keys = list(sorted_res.keys())

         i=0
         while i < k:
             ret.append(keys[i])
             i += 1
        
         return ret

            
            
        

        
        