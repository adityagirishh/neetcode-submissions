class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = []
        for i in set(nums):
            freq.append((nums.count(i),i))
        n = len(freq)
        freq.sort(reverse=True)
        res=[]
        for i in range(k):
            res.append(freq[i][1])
        return res
        
        


        



        

        


