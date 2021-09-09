## 1. Sort the following functions in decreasing order of asymptotic complexity ($O(f(n))$):
- $f_1(n) = n^{\sqrt{n}}$
- $f_2(n) = 2^n$
- $f_3(n) = {n\choose 2}$
- $f_4(n) = \sum_{i=2}^n (i-1)$

### Answer:
#### $f_2(n) \leq f_1(n) \leq f_4(n) \leq f_3(n)$
--------
## 2. Implement in Python the insertion sort procedure to sort into non-increasing instead of non-decreasing order
- 2.1 Use the time function to measure the execution time for the best and worst inputs of size between 10 and 1,000 (use steps of 10)
- 2.2 Plot the best and worst execution times measured in (2.1) as a function of $n$
- 2.3 Use the random function to generate randomly sorted inputs to calculate the execution time. For each $n$ run the program for 100 different inputs. Do for $n = 100,200, \dots, 1000$.
- 2.4 Plot the mean, median, and standard deviation as a function of $n$ for the values obtained in 2.3
### Answer:
#### See exercise2.py for answer
--------
## 3. CLRS 2.1-4
pg. 22: Consider the problem of adding two n-bit binary integers, stored in two n-element arrays A and B. The sum of the two integers should be stored in binary form in an .n C 1/-element array C. State the problem formally and write pseudocode for adding the two integers.
### Answer:
#### Input:
$A = [a_1,a_2,\dotsc,a_n]$ donde $a_n$ son booleanos,

$B= [b_1,b_2,\dotsc,b_n]$ donde $b_n$ son booleanos.

Output:
$C = [c_1,c_2,\dotsc,c_{n+1}]$ donde $c_n$ es la suma de $a_n + b_n$  
####
#### Pseudocode:
    function bin_sum(A,B):
        // Binary sum algorithm
        C = int[A.length + 1]
        carry = 0
        for i = 1 to A.length:
            C[i] = (A[i] + B[i] + carry) % 2 
            carry = (A[i] + B[i] + carry) / 2
        C[i + 1] = carry
        return C
--------
## 4. CLRS 3.1-1
pg. 52: Let $f(n)$ and $g(n)$ be asymptotically nonnegative functions. Using the basic definition of ‚$\theta$-notation, prove that $max(f(n), g(n)) = \Theta(f(n) + g(n))$.

### Answer:
####
Primero, debemos encontrar los valores: $c_1,c_2$ y $n_0$:

$0 \leq c_1f(n) + g(n) \leq max(f(n),g(n)) \leq c_2(f(n)+g(n))$

De aqui podemos deducir que $f(n) \geq 0$ y $g(n) \geq 0$, lo que demuestra que $n \geq n_0$ 

Tambien podemos decir que:

$f(n) + g(n) = 2 \times max(f(n),g(n))$

porque $f(n)$ y $g(n) \geq max(f(n),g(n))$ 

Ahora solo resolvemos:

$0 \leq 1/2(f(n) + g(n)) \leq max(f(n),g(n)) \leq c_2(f(n)+g(n))$ para $n \geq n_0$

Por lo tanto:

$max(f(n), g(n)) = \Theta(f(n) + g(n))$ ya que $c_1 = 1/2$ y $c_2 = 1$
####
--------
## 5. CLRS 3.1-2
pg. 52: Show that for any real constants a and b, where $b>0$, ${(n+a)}^b = \theta(n^b)$.
### Answer:
####
Definimos la ecuacion con las incognitas $c_1, c_2$ y $n_0$:

$0 \leq c_1n^b \leq {(n+a)}^b \leq$ cuando $n \geq n_0$

Sabemos que $n+a > n$, de esta forma:

$n+a \leq 2n$ tal que $|a| \leq n$

$n/2 \geq |a|$ de modo que $n_0 = 2|a|$

Reemplazamos: $0 \leq {(n/2)}^b \leq {(n+|a|)}^b \leq 2n^b$

Lo que demuestra que:

${(n+a)}^b = \Theta(n^b)$ con $c_1 = (1/2)^b, c_2=2^b$ y $n_0=2|a|$

####
--------
## 6. CLRS 3.1-6
pg. 53: Prove that the running time of an algorithm is $\Theta(g(n))$ if and only if its worst-case
running time is $O(g(n))$ and its best-case running time is $\Omega(g(n))$

### Answer:
####
Suponemos que existe $f(n) = \Theta(g(n))$,

Podemos determinar los limites con la inecuacion cuando $n \geq n_0$, de esta forma:

Limite inferior (best case): $c_2g(n)$
Limite superior (worst case): $c_1g(n)$

Reescribimos la ecuacion:

$0 \leq c_1g(n) \leq f(n) \leq c_2g(n)$

$0 \leq f(n) \leq c_2g(n)$ que muestra $f(n) = O(g(n))$ 

$0 \leq c_1g(n) \leq f(n)$ que muestra $f(n) = \Omega(g(n))$,

que es lo que queriamos demostrar para el mejor y peor de los casos
####
--------
## 7. CLRS 3-4 (a,b,e,g)
pg. 62: Let $f(n)$ and $g(n)$ be asymptotically positive functions. Prove or disprove each of
the following conjectures:

  - a) $f(n) = O(g(n))$ implies $g(n) = O(f(n))$
  - b) $f(n) + g(n) = \Theta(min(f(n),g(n)))$
  - e) $f(n) = O((f(n))^2)$
  - g) $f(n) = \Theta(f(n/2))$

### Answer:
a) 

Si suponemos que $f(n) = n$ y $g(n) = n^2$, $f(n) = O(g(n))$ se puede decir que es verdadera. Pero $n^2 \neq O(n)$, por ende es falso.

b)

Si establecemos $f(n) = n$ y $g(n) = 1$, $n+1 \neq \Theta(min(f(n),g(n)))$, por ende es falso.

e)

$0 \leq f(n) \leq c(f(n))^2$ donde $f(n) = O(f(n))^2$, esto solo se cumple si $f(n) \geq 1$.

g)

Si definimos la ecuacion con sus constantes $c_1,c_2$ y $n_0$, y establecemos $f(n) = 2^n$ si $n \geq n_0$, reemplazamos:

$0 \leq c_12^{n/2} \leq 2^n \leq c_22^{n/2}$, se muestra que es falso.