class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
        a = [0]*len(nums)
        for i in range(len(nums)):
            if(nums[i]==a[i]):
                return False
            else:
                a[i]=nums[i]

         