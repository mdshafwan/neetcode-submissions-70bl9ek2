class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a={}
        output = []
        
        for i in nums:
            a[i]=a.get(i,0)+1
        
        for i,j in a.items():
            output.append([j,i])
        output.sort()

        res = []
        while len(res) < k:
            res.append(output.pop()[1])
        
        return res