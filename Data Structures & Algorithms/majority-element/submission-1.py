class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm={}
        for i in nums:
            if i in hm:
                hm[i]+=1
            else:
                hm[i]=1
        for key,value in hm.items():
            if value>len(nums)//2:
                return key