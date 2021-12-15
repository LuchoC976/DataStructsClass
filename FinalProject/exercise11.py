# 11. Given an integer n, return all the strobogrammatic numbers that are of length n.
# You may return the answer in any order.

import unittest

def TestValue_results():
    assert solve(0) == [""], "Should be ['']"
    assert solve(1) == ["0", "1", "8"], "Should be ['0', '1', '8']"
    assert solve(2) == ["11","69","88","96"], "Should be ['11','69','88','96']"
    assert solve(-1) == [""], "Should be ['']"
    assert solve(3) == ['101','111','181','609','619','689','808','818','888','906',
    '916','986'], "Should be ['101','111','181','609','619','689','808','818','888','906','916','986']"
    
def solve(n):
    result = strobogrammaticSolver(n, n)

    result.sort()
    return result

def strobogrammaticSolver(n, n2):
    if n <= 0:
        return [""]
    elif n == 1:
        return ["0", "1", "8"]
    
    body = strobogrammaticSolver(n-2, n2)
    final = []

    for item in body:
        if n != n2:
            final.append("0" + item + "0")

        final.append("1" + item + "1")
        final.append("6" + item + "9")
        final.append("8" + item + "8")
        final.append("9" + item + "6")
    
    return final

if __name__ == "__main__":
    TestValue_results()
    print("All test cases passed")

'''
Para determinar que un numero es estrobogramatico,
debe verse igual a 0 grados de rotacion y a 180 grados
de rotacion. Los numeros que se ven de esta forma entre 
el 0 y 9 son: 0, 1 y 8. Para el resto de casos se utilizaran
pares de numeros que cumplan la condicion. Estos pares son:
00, 11, 69, 88 y 96.
El problema funciona de tal manera que utilizamos recursion
para llenar la seccion de la mitad del numero con valores
simples, luego, se va rompiendo de regreso la recursion y
se añaden los pares de valores que satisfacen la condicion,
de tal forma que uno de los numeros va al extremo izquierdo
y el otro al extremo derecho.
Los casos base de la recursion son para los valores de 
0 y 1, donde se retornan los centros de cada numero y cuando
se rompe la recursion hacia arriba, se añaden los extremos
al centro hasta que se termina por completo el proceso.
'''