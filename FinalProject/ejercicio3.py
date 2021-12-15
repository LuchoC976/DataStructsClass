import unittest

def TestValue_results():
    
    assert outputArray([1,3,4,2,2]) == 2, "Should be 2"
    assert outputArray([3,1,3,4,2]) == 3, "Should be 3"
    assert outputArray([1,1]) == 1, "Should be 1"
    assert outputArray([1,1,2]) == 1, "Should be 1"
    assert outputArray([4,2,2,1]) == 2, "Should be 2"
    
    


#ordenamos el arreglo que nos presenten
#recorremos por puestos el array "importante"
#comparamos si el segundo puesto es igual al primero y retornamos
def outputArray (array):
    array.sort();
    for i in range ( 1, len (array) ):
        if array [i] == array [ i-1 ]:
            return array [i];
        
#print(outputArray([4,2,2,1]));



if __name__ == "__main__": 
    
    TestValue_results()
    print("All test cases passed")