class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        result = []
        for i in nums:
            res[i] +=1
        frq = list(res.values())
        frq.sort(reverse=True)
        for ele,ct in res.items():
            if ct in frq[:k]:
                result.append(ele)
        return (result)
        


        



        

        


