# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # self_print_p=[]
        self.self_print=[]

        def dfs(root):
            if not root:
                self.self_print.append(None)

                return
            
            self.self_print.append(root.val)
            dfs(root.left)

            
            dfs(root.right)

        dfs(p)
        test_p=self.self_print
        self.self_print=[]
        dfs(q)
        test_q=self.self_print
        return True if test_p==test_q else False