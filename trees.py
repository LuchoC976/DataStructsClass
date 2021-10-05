# Trees implementation in Python

# Preorder, inorder, postorder traversals
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
    
    def inorderTraversal(self):
        final = []

        def visit(start, arr):
            if start.left:
                visit(start.left, arr)

            if start:
                arr.append(start.val)
            
            if start.right:
                visit(start.right, arr)
        
        visit(self.root, final)
        return final
    
    def postorderTraversal(self):
        final = []

        def visit(start, arr):
            if start.left:
                visit(start.left, arr)
            
            if start.right:
                visit(start.right, arr)

            if start:
                arr.append(start.val)

        visit(self.root, final)
        return final

# Tree implementation
myTree = BinaryTree(TreeNode("A"))

myTree.root.left = TreeNode("B")
myTree.root.left.left = TreeNode("C")
myTree.root.left.right = TreeNode("D")
myTree.root.right = TreeNode("E")
myTree.root.right.left = TreeNode("F")
myTree.root.right.left.left = TreeNode("G")
myTree.root.right.left.right = TreeNode("H")
myTree.root.right.right = TreeNode("I")

print(
'''
Tree 1 View:
                 [A]
               /     \ 
            [B]       [E]
           /   \     /   \ 
         [C]   [D]  [F]  [I]
                   /   \ 
                 [G]   [H]
'''
)

# Preorder traversal
print("Preorder traversal 1: ")
print(myTree.preorderTraversal())

# Inorder traversal
print("Inorder traversal 1: ")
print(myTree.inorderTraversal())

# Postorder traversal
print("Postorder traversal 1: ")
print(myTree.postorderTraversal())

# Tree 2 test
myTree2 = BinaryTree(TreeNode(1))

myTree2.root.left = TreeNode(2)
myTree2.root.right = TreeNode(3)
myTree2.root.left.left = TreeNode(4)
myTree2.root.left.right = TreeNode(5)

print(
'''
Tree 2 View:
                [1]
               /   \ 
            [2]     [3]
           /   \     
         [4]   [5]
'''
)

# Preorder traversal
print("Preorder traversal 2: ")
print(myTree2.preorderTraversal())

# Inorder traversal
print("Inorder traversal 2: ")
print(myTree2.inorderTraversal())

# Postorder traversal
print("Postorder traversal 2: ")
print(myTree2.postorderTraversal())