class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        for i in range(len(nums)):
            out=1
            for j in range(len(nums)):
                if j == i:
                    continue
                else:
                    out*=nums[j]
            output.append(out)
        return output



        