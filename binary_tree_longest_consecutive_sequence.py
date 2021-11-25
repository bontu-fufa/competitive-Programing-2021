# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        def longest(node , prev_node , length):

            if not node: return length
            
            if prev_node + 1 == node.val: curr_len = length + 1
            else: curr_len = 1
                
            left_len = longest(node.left , node.val, curr_len)
            right_len = longest(node.right, node.val, curr_len)
            
            return max(left_len , right_len, length) 
        
        if root: return longest(root ,root.val - 1, 0)