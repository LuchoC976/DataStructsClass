from typing import DefaultDict

def TestValue_results():
    assert solve([2,4,6,8,10]) == 7, "Should be 7"
    assert solve([7,7,7,7,7]) == 16, "Should be 16"
    assert solve([3,6,9,12,18]) == 4, "Should be 4"
    assert solve([1,2,3]) == 1, "Should be 1"
    assert solve([10]) == 0, "Should be 0"

def solve(arr) :
    n = len(arr)
    dp = [DefaultDict(int) for _ in range(n)]
    output = 0

    for i in range(n):
        for j in range(i):
            diff = arr[i] - arr[j]
            dp[i][diff] += (1 + dp[j][diff])
            output += dp[j][diff]
    
    return output
    
if __name__ == "__main__":
    TestValue_results()
    print("All test cases passed")

'''
Para este problema tuve que investigar acerca del tema de
programacion dinamica, en donde utilizamos un arreglo para
realizar nuestros calculos que son los siguientes: 
Se utilizo la estructura de datos de diccionarios (hash map)
para simular cuantas subsecuencias existian dentro de un
mismo arreglo. La clave de cada diccionario dentro del arreglo
seria el valor i de inicio y el valor j seria el valor que 
persigue al valor de inicio. 
A medida que se avanza en el arreglo, para cada posicion se
calcula la diferencia (diff) entre el valor i y j para 
determinar si son subsecuentes. Si se cumple esta condicion,
se agrega 1 al valor del diccionario en la posicion de i.
Estos valores se van acumulando y por eso se suman a la cantidad
que habia previamente. Cuando se termina de recorrer el arreglo,
sumamos la cantidad de sucesiones que estan en la clave de cada
diccionario en cada posicion y se retorna el entero final.
'''

 
