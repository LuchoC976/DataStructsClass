import unittest

def TestValue_results():
    
    cir = ListCir();
    cir1 = ListCir();
    cir2 = ListCir();
    cir3 = ListCir();
    cir4 = ListCir();

    assert cir.respuesta([3,4,1], 2) == [3, 4, 1, 2], "Should be [3, 4, 1, 2]"
    assert cir1.respuesta([5, 5, 1], 3) == [5, 5, 1, 3], "Should be [5, 5, 1, 3]"
    assert cir2.respuesta([3,2,2], 1) == [3, 2, 2, 1], "Should be [3, 2, 2, 1]"
    assert cir3.respuesta([6, 6, 2], 7) == [6, 6, 2, 7], "Should be [6, 6, 2, 7]"
    assert cir4.respuesta([5, 5, 2], 1) == [5, 5, 2, 1], "Should be [5, 5, 2, 1]"
    

class Nodo:
    def __init__(self, val = None):
        self.val = val;
        self.next = None;

class ListCir:
    def __init__(self):
        self.first = None;
    
    def vacio (self):
        return self.first is None;

    def insert (self, dato):
        aux = Nodo (dato);
        if (self.first is None):
            self.first = aux;
            aux.next = self.first;
        auxDos = self.first;
        while (auxDos.next != self.first):
            if (auxDos.next.val >= dato and auxDos.val < dato):
                aux.next = auxDos.next;
                auxDos.next = aux;
                return True;
            auxDos = auxDos.next;
        aux.next = self.first;
        auxDos.next = aux;
        return True;

    def insertBasic (self, dato):
        for i in dato:
            aux = Nodo (i);
            if (self.first is None):
                self.first = aux;
                aux.next = self.first;
            auxDos = self.first;
            while (auxDos.next != self.first):
                auxDos = auxDos.next;
            aux.next = self.first;
            auxDos.next = aux;

    def imprimir (self):
        auxList = [];
        aux = self.first;
        while (aux.next != self.first):
            auxList.append(aux.val);
            aux = aux.next;
        auxList.append(aux.val);
        return auxList;

    def respuesta (self, lista, dato):
        self.insertBasic(lista);
        self.insert(dato)
        return self.imprimir();

#generamos el nodo circulo y la lista circulo
#el insertar basico nos permite generar la lista circular que nos envian como parametro
#recorriendo toda la lista circular y agregando al final los nuevos elementos
#la funcion insertar es similar al insertarBasico pero toma en cuenta si el numero es menor
#o igual a la posicion siguiente y si la posicion actual es es menor al dato insertado
#por ultimo la funcion imprimir permite recorrer toda la lista tomando sus valores




if __name__ == "__main__": 
    
   TestValue_results()
   print("All test cases passed")
    
