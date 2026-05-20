class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        for i in nums:
            if i in hm:
                hm[i]+=1
            else:
                hm[i]=1
        sort_items=sorted(hm.items(), key=lambda x: x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(sort_items[i][0])
        return result     