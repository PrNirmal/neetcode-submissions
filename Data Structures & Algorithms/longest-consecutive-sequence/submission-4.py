class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        list_new=list(set(nums))
        list_new.sort()
        cnt=1
        res=1
        for i in range(1,len(list_new)):
            if list_new[i-1]+1==list_new[i]:
                cnt+=1
            else:
                cnt=1
            res=max(res,cnt)
        return res
