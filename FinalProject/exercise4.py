# 4. You have observations of n + m 6-sided dice rolls with
# each face numbered from 1 to 6. n of the observations 
# went missing, and you only have the observations of m rolls. 
# Fortunately, you have also calculated the average value of the n + m rolls.

import unittest

def TestValue_results():
    assert solve([3,2,4,3], 4, 2) == [6,6], "Should be [6,6]"
    assert solve([1,5,6], 3, 4) == [2,2,2,3], "Should be [2,2,2,3]"
    assert solve([1,1,4,1,2], 3, 8) == [3,3,3,3,3,3,3,9], "Should be [3,3,3,3,3,3,3,9]"
    assert solve([1,2,3,1], 2, 1) == [3], "Should be [3]"
    assert solve([1,1,2,5,6], 2, 4) == [0], "Should be [0]"

def solve(rolls, mean, n):
    m = len(rolls)
    num = (m + n) * mean - sum(rolls)
    mult = num % 6
    div = num // n

    if num < n or num > n * 6: 
        return [0]

    if mult <= 6:
        start = num // n
        end = num - start * (n - 1)
        return [start] * (n - 1) + [end]
    else:
        carry = num - (div) * (n - 1) - 6
        start = div
        mid = start + 1
        end = num - start * (n - 1 - carry) - mid * carry

        return [start] * (n - 1 - carry) + [mid] * carry + [end]
    
if __name__ == "__main__":
    TestValue_results()
    print("All test cases passed")

'''
Para este problema hay que tomar en cuenta muchas cosas:
El tamaño del array, la media y el numero total de lanzamientos.
La variable 'num' representa la suma que falta para cumplir con
la media que se pasa como argumento. Por lo tanto, si este valor 
es menor al numero de dados que quedan o mayor al numero de dados
que quedan por 6 (numero de caras), se pasa un arreglo con valor [0]
ya que es imposible calcular para ese caso.
Lo que se hace en este problema es calcular un valor donde vamos a iniciar
la cuenta (start), y un valor donde se termina (end), es decir un valor minimo
y maximo para agregar al arreglo final. Se retorna el primer caso repetido
un numero de (n-1) veces ya que aun falta un ultimo valor que sera el maximo.
Esto se hace cuando el numero que queda (num) por agregar, es multiplo de 6.
Para el otro caso en donde (num) no es multiplo de 6, se toma igual un punto
de inicio y otro de final, la diferencia para este caso es que debemos calcular
los valores que van entre estos dos numeros y se toma un resto (carry), donde
se simula el valor minimo a repetirse un numero (carry) de veces empezando por
el valor de inicio agregado 1 y se retorna el valor de inicio, los valores del
medio y el valor final.
'''