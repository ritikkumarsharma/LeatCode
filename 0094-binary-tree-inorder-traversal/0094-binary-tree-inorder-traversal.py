
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ritik = []
        def inorder(root, ritik):
            if not root:
                return None
            inorder(root.left,ritik)
            ritik.append(root.val)
            inorder(root.right,ritik)
        inorder(root,ritik)
        return ritik