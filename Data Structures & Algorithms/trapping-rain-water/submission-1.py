class Solution:
    def trap(self, height: List[int]) -> int:
        out=0
        left,right=0,len(height)-1
        leftmax,rightmax=height[left],height[right]
        
        while left<right:
            if leftmax<rightmax:
                left+=1
                leftmax=max(leftmax,height[left])
                out+=leftmax-height[left]
            else:
                right-=1
                rightmax=max(rightmax,height[right])
                out+=rightmax-height[right]

        return out