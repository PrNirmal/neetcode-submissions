class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output=[0]*len(temperatures)
        stack=[]

        for idx,temp in enumerate(temperatures):
            while stack and temp>stack[-1][1]:
                stackidx,stacktem=stack.pop()
                output[stackidx]=idx-stackidx
            stack.append((idx,temp))
        return output