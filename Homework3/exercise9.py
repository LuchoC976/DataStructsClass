# 9. Tenemos un árbol binario (binary tree), definimos a un nodo X como 
# rojo, si todos los nodos en el recorrido de la raiz al nodo X 
# tienen un valor que es menor o igual a X. Por ejemplo, en el ejemplo de abajo:

# Escriba una función en Python que cuente el numero total de nodos rojos. El input
# de esta función es la raíz del árbol binario.

class TreeNode:
    def __init__(self, val=0, left=0, right=0):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root):
        self.root = root
    
    def countRedNodes(self):
        final = []
        redNodeCount = 0
        if self.root == None:
            return 0
        
        # Stack simulation with list
        nodeStack = []
        nodeStack.append(self.root)

        max_val = nodeStack[0].val
        while (len(nodeStack) > 0):
            # Remove stack values
            node = nodeStack.pop()

            if node.val <= max_val:
                redNodeCount += 1

            # Append to returned list of TreeNode.values
            final.append(node.val)

            # If right, add to stack so you can check left first (since left is at top)
            if node.right:
                nodeStack.append(node.right)
            if node.left:
                nodeStack.append(node.left)
        
        return redNodeCount

root = TreeNode(3)
root.left = TreeNode(1)
root.left.left = TreeNode(3)
root.right = TreeNode(4)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)


tree = BinaryTree(root)

'''
                [[3]]
               /     \ 
            [1]      [[4]]
           /         /   \ 
        [[3]]      [1]  [[5]]
return = 4
'''

print("Red Node Count: " + str(tree.countRedNodes()))