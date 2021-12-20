import unittest

def TestValue_results():
    
    assert arrayImp([1,3,5]) == 4, "Should be 4"
    assert arrayImp([2,4,6]) == 0, "Should be 0"
    assert arrayImp([3, 3, 2]) == 3, "Should be 3"
    assert arrayImp([8,1,2]) == 4, "Should be 4"
    assert arrayImp([7,3,4]) == 3, "Should be 3"

# Implementacion del array
def arrayImp (list):
    retTotal = 0;
    sumTotal = 0;
    cont = 0;
    tiempos = 0;
    for val in list:
        sumTotal += val;
        if sumTotal % 2 == 0:
            retTotal += cont;
            tiempos += 1;
        else:
            retTotal += 1 + tiempos;
            cont += 1;
    
    return retTotal  % (10**9 + 7);

#nos valemos de las propiedades de los numeros que dos numeros pares siempre daran un par
#y un impar con un par dara un impar, y dos impares dara un par
#recorremos el arreglo y vamos sumando sus valores, analizamos esa suma para saber si 
#la suma da un numero por o impar, en caso de dar un numero par nuestra variable retTotal 
#la sumamos con nuestro contador de numero impares "cont"
#y sumamos un tiempo a la cantidad de numeros pares que hay 
#de dar un numero impar sumamos sumamos 1 mas la cantidad de tiempos pares que existen anteriormente
#y finalmente añadimos un contador a los numero impares
#luego de recorrer todo el arreglo retornamos en base a lo que nos pide el ejercicio



if __name__ == "__main__": 
    
   TestValue_results()
   print("All test cases passed")
    
