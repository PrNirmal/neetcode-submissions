class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # check_dict={}
        mp=dict(Counter(nums))
        
        list_1=list(mp.items())

        list_1.sort(key=lambda x:(x[1],x[0]),reverse=True)
        output=[]
        for i in range(k):
            output.append(list_1[i][0])
        return output