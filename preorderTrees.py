# Preorder traversal in trees
class TreeNode:
    def __init__(self, val=0, left=0, right=0):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root):
        self.root = root
    
    def preorderTraversalRecursive(self):
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

    def preorderTraversalStack(self):
        final = []
        if self.root == None:
            return 0
        
        # Stack simulation with list
        nodeStack = []
        nodeStack.append(self.root)

        while (len(nodeStack) > 0):
            # Remove stack values
            node = nodeStack.pop()
            # Append to returned list of TreeNode.values
            final.append(node.val)

            # If right, add to stack so you can check left first (since left is at top)
            if node.right:
                nodeStack.append(node.right)
            if node.left:
                nodeStack.append(node.left)
        
        return final
    
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
Tree View:
                 [A]
               /     \ 
            [B]       [E]
           /   \     /   \ 
         [C]   [D]  [F]  [I]
                   /   \ 
                 [G]   [H]
'''
)

# Preorder recursive traversal
print("Preorder recursive traversal: ")
print(myTree.preorderTraversalRecursive())

# Preorder iterative (stacks) traversal
print("Preorder iterative (stacks) traversal: ")
print(myTree.preorderTraversalStack())