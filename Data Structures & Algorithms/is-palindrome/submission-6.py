class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        # s.replace(" ","")
        while left<right:
            if not(s[left].isalnum()) or s[left]==" ":
                left+=1
                continue
            if not(s[right].isalnum()) or s[right]==" ":
                right-=1
                continue
            if s[left].casefold()==s[right].casefold():
                left+=1
                right-=1
            else:
                return False
        return True