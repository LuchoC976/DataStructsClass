import unittest

def TestValue_results():
    
    p11 = respuesta();

    tree1 = NodoArbol(3);
    tree1.left = NodoArbol (9);
    tree1.right = NodoArbol (20);
    tree1.right.left = NodoArbol (15);
    tree1.right.right = NodoArbol (7);
   
    
    tree2 = NodoArbol(3);
    tree2.left = NodoArbol (9);
    tree2.right = NodoArbol (8);
    tree2.left.left = NodoArbol (4);
    tree2.left.right = NodoArbol (0);
    tree2.right.left = NodoArbol (1);
    tree2.right.right = NodoArbol (7);
    
    tree3 = NodoArbol(3);
    tree3.left = NodoArbol (5);
    tree3.right = NodoArbol (5);
    tree3.left.left = NodoArbol (4);
    tree3.left.right = NodoArbol (1);
    tree3.right.left = NodoArbol (1);
    tree3.right.right = NodoArbol (0);
    
    tree4 = NodoArbol(2);
    tree4.left = NodoArbol (2);
    tree4.right = NodoArbol (10);
    tree4.right.left = NodoArbol (1);
    tree4.right.left.right = NodoArbol (8);
    
    tree5 = NodoArbol(3);
    tree5.left = NodoArbol (9);
    tree5.right = NodoArbol (8);
    tree5.left.left = NodoArbol (4);
    tree5.left.right = NodoArbol (0);
    tree5.right.left = NodoArbol (1);
    tree5.right.right = NodoArbol (7);
    tree5.left.right.left = NodoArbol (5);
    tree5.right.left.right = NodoArbol (2);


    

    assert p11.imprTransversa(tree1) == [[9],[3,15],[20],[7]], "Should be [[9],[3,15],[20],[7]]"
    assert p11.imprTransversa(tree2) == [[4], [9], [3, 0, 1], [8], [7]], "Should be [[4], [9], [3, 0, 1], [8], [7]]"
    assert p11.imprTransversa(tree3) == [[4], [5], [3, 1, 1], [5], [0]], "Should be [[4], [5], [3, 1, 1], [5], [0]]"
    assert p11.imprTransversa(tree4) == [[2], [2, 1], [10, 8]], "Should be [[2], [2, 1], [10, 8]]"
    assert p11.imprTransversa(tree5) == [[4], [9, 5], [3, 0, 1], [8, 2], [7]], "Should be [[4], [9, 5], [3, 0, 1], [8, 2], [7]]"



import collections
class NodoArbol(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class respuesta(object):
    def imprTransversa(self, root: NodoArbol):
        def buscar(node: NodoArbol, x: int, y: int):
            if not node:
                return
            nodSoporte[x].append((-y, node.val))
            buscar(node.left, x - 1, y - 1)
            buscar(node.right, x + 1, y - 1)

        ans = []
        nodSoporte = collections.defaultdict(list)

        buscar(root, 0, 0)

        for z, nodes in sorted(nodSoporte.items(), key=lambda item: item[0]):
            ans.append([val for z, val in sorted(nodes)])

        return ans

#definimos el nodo arbol y llenamos sus valores
#creamos una funcion recursiva y le pasamos los valores del nodo
#tanto como las coordenadas en "x" y "y"
#agregamos al defaultdict el valor en la cordenada "y" y el valor del nodo
# al final recorremos el nodSoporte y almacenamos estos valores en la variable ans
#como los valores de nodes en este punto son "diccionarios" los separamos en llave valor y tomamos el valor
#retornamos los valores finales





if __name__ == "__main__": 
    
    TestValue_results()
    print("All test cases passed")