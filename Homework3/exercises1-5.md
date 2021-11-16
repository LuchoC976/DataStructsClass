# 1. Una función recursiva resuelve un problema resolviendo una parte mas pequeña del mismo problema.
Verdadero, porque la definición de recursión pide que calculemos el caso base y un factor de cambio. La recursión es un ejemplo de Divide and Conquer, que resuelve partes más pequeñas de un problema haciéndolo más simple.

# 2. Los modelos computacionales nos ayudan a analizar la complejidad de los algoritmos, ya que nos proveen de las especificaciones de la computadora en la cual estos se ejecutarían idealmente.
Verdadero, ya que un modelo computacional expresa cuanto tiempo tomará cada operación que realicemos, de esta forma, solo sumamos para obtener el mejor y peor de los casos y así logramos obtener la complejidad.

# 3. La búsqueda en un árbol binario de búsqueda es siempre mas rápida que la búsqueda lineal en un arreglo.
Falso, normalmente es más rápida que la búsqueda lineal en un arreglo (complejidad log(n)) para el mejor de los casos (balanced BST). Pero si el numero de nodos N es igual a la altura H del BST, la complejidad se vuelve O(n), haciendo que no siempre sea más rápido que una búsqueda lineal, a veces puede ser igual de rápido.

# 4. Un algoritmo de complejidad $Ω(nlog(n))$ es mas rápido que un algoritmo de complejidad $Ω(n)$.
Falso, ya que $Ω(nlog(n))$ y $Ω(n)$ siguen siendo complejidades como $O(n)$. Por lo tanto, $O(nlog(n))$ es menos rápida que un algoritmo de complejidad $O(n)$.

# 5. Un algoritmo de complejidad $O(nlog(n))$ es mas rápido que un algoritmo de complejidad $O(n)$.
Falso, $O(n)$ es más rápido que un algoritmo $O(nlog(n))$. Los única complejidad más rápida que la lineal es: $O(log(n))$