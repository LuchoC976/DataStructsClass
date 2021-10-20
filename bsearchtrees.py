# BST
# Binary search trees implementation

class TreeNode:
    def __init__(self, val=0, left=0, right=0):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root):
        self.root = root
    def preorderTraversal(self):
        final = []

        def visit(start, arr):
            if start:
                arr.append(start.val)
            
            if start.left:
                visit(start.left, arr)
            
            if start.right:
                visit(start.right, arr)
        
        visit(self.root, final)
        return final

    def BST_search(self, root, value):
        if not root:
            return False
        if root.val == value:
            return True

        if root.val > value:
            self.BST_search(root.left, value)
        else:
            self.BST_search(root.right, value)

myTree = BinaryTree(TreeNode(4))

myTree.root.left = TreeNode(2)
myTree.root.left.left = TreeNode(1)
myTree.root.left.right = TreeNode(3)
myTree.root.right = TreeNode(6)
myTree.root.right.left = TreeNode(5)
myTree.root.right.right = TreeNode(8)
myTree.root.right.right.left = TreeNode(7)
myTree.root.right.right.right = TreeNode(9)

print(myTree.BST_search(myTree.root, 5))

