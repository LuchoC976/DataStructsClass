from typing import DefaultDict
from collections import deque
import unittest

def TestValue_results():
    assert solve(5, [[0,1],[1,2],[2,3],[3,4]]) == 1, "Should be 1"
    assert solve(5, [[0,1],[1,2],[3,4]]) == 2, "Should be 2"
    assert solve(1, [[0,1],[1,3],[2,3],[5,7]]) == 0, "Should be 0"
    assert solve(3, [[0,1], [1,2], [0,2]]) == 1, "Should be 1"
    assert solve(1, [[0,0]]) == 1, "Should be 1"

def solve(n, edges):
    graph = DefaultDict(list)
    visited = set()
    count = 0

    if n < len(edges):
        return 0

    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)

    def bfs(node):
        q = deque()
        q.append(node)
        visited.add(node)
        while q:
            curr = q.popleft()
            for item in graph[curr]:
                if item not in visited:
                    visited.add(item)
                    q.append(item)
    
    for node in range(n):
        if node not in visited:
            bfs(node)
            count += 1
    
    return count

if __name__ == "__main__":
    TestValue_results()
    print("All test cases passed")
    
'''
Para este problema segui una solucion de BFS,
en donde se chequea cada edge que tiene el nodo (que
entra como argunmento) y se los va añadiendo a una cola
de manera recursiva. Es decir que para cada nodo se toma 
en cuenta sus edges y se va chequeando si los nodos estan
conectados entre si. Si existen nodos que pertenecen al grafo
pero aun no entran en la recursion significa que estan separados.
Cada vez que termina el proceso recursivo, se suma 1 a la
cuenta de componentes conectados y se retorna finalmente
una vez que ya hayan pasado por la recursion todos los nodos
del grafo.
Se utilizo grafos, recursion, BFS, colas y diccionarios (hash map)
para chequear los nodos conectados por cada key (nodo).
'''