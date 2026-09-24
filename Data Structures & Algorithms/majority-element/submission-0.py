class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        res = defaultdict(int)
        for i in nums:
            res[i]+=1
        for num,count in res.items():
            if count > n/2:
                return num