class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hset = {}
        lucky = -1
        for i in range(len(arr)):
            hset[arr[i]] =  hset.get(arr[i],0)+1

        for i in range(len(arr)):
            if arr[i] == hset[arr[i]]:
              lucky=max(lucky,arr[i])
  
        return lucky
       
