1. Crie a função python def taboada(n):
Apresenta a taboada do inteiro n, onde 1 <= n <= 9, que reproduz a taboada do número `n` na forma (exemplo para `n` = 7):
#Taboada do 7
# 0 x  7 =  0
# 1 x  7 =  7
# 2 x  7 = 14
# 3 x  7 = 21
# 4 x  7 = 28
# 5 x  7 = 35
# 6 x  7 = 42
# 7 x  7 = 49
# 8 x  7 = 56
# 9 x  7 = 63
# 10 x  7 = 70

2. Implemente uma função que receba um valor `n` inteiro e imprima até a n-ésima linha da seguinte forma:
  1
  2   2
  3   3   3
  :   :   :
  n   n   n   n   n   n  ... n

3. Implemente uma função que receba um valor `n` inteiro e imprima até a n-ésima linha da seguinte forma:
 1
 1   2
 1   2   3
 :   :
 1   2   3 ... n

4. Implemente uma função que receba um valor em segundos e imprima o correspondente em horas, minutos e segundos. Por exemplo, se a função receber como argumento 4814, imprimirá 1 hora(s) 20 minuto(s) e 14 segundo(s).

5. Implemente uma função que retorna `True` se o argumento de entrada for um número natural primo e `False` caso contrário.

6. Implemente uma função que retorne a quantidade de dígitos de um determinado número natural passado como argumento. Por exemplo, ao chamar a função com o número 2131, ela deverá retornar 4. Usar apenas operações matemáticas, isto é, não usar operações com strings.

7. Implemente uma função que recebe um numero inteiro e retorne este número escrito ao contrário:
Entre com um numero inteiro: 12345
O seu inverso: 54321
Desenvolva a funcao sem recorrer a operacoes com strings, isto é, utilize apenas operações matemáticas
Inverte Numero
Implemente uma função que recebe um numero inteiro e retorne este numero escrito ao contrario:
Entre com um numero inteiro: 12345
O seu inverso: 54321
Desenvolva a funcao sem recorrer a operacoes com strings.
Utilize apenas operacoes matematicas

8. Implemente a função `todos_iguais(sequencia)` que retorna `True` se todos os elementos de `sequencia` forem iguais, e retorna `False` caso contrário.

9. Implemente a função `todos_diferentes(sequencia)` que retorna `True` se todos os elementos de `sequencia` forem diferentes entre si, e retorna `False` caso contrário, isto é, pelos menos um elemento seja igual a outro componente da `sequencia`.

10. Implemente uma função que recebe como argumentos um número `n` e uma lista de números, `indice_elemento(n, lista)`. A função retornará o índice da primeira ocorrênia do número na lista e `-1` se o número não estiver na lista. Obs: em Python, índices de listas, arrays, etc. começam em `0`.

11. Implemente uma função que recebe um número `n` e retorna a menor potência de 2 maior ou igual a `n`. Por exemplo, `pot2(14)` retornará `16`,  `pot2(42)` retornará `64`. Obs: um algoritmo como esse é usado em processamento de sinais para determinar a ordem da transformada rápida de Fourier.

12. Implemente uma funçao que dado um número natural maior do que `1`, decomponha esse número em fatores primos. Por exemplo, se o argumento de entrada for 36, a saída deverá ser [2, 2, 3, 3], porque $2 \times 2 \times 3 \times 3 = 36$.

13. Implemente a função `maiorN(lista, N)` que recebe uma lista de números quaisquer, um valor `N`, `1 <= N <= len(lista)`,  e retorna o Nésimo maior valor na lista de números. Por exemplo, se `N` for `1`, retorna o maior valor na lista, se `N` for `2`, retorna o segundo maior valor na lista, etc. Exemplo:
lista = [5, -1, 7, 0, -3, 9]
N = 2
print(f'Em {lista} o {N}o. maior valor é {maiorN(lista, N)}')

14. Implemente uma função recursiva `div(m, n)` que recebe como argumentos dois números naturais `m` e `n` e devolve o resultado da divisão inteira de `m` por `n`. Não pode recorrer às operações aritméticas de multiplicação, divisão inteira e resto da divisão inteira.

15. Implemente uma função que recebe o seu peso e altura e retorna seu índice de massa corporal, IMC. A função também deverá emitir a classificação, de acordo com a tabela abaixo:

IMC|CLASSIFICAÇÃO
---|-------------
MENOR QUE 18,5|	MAGREZA
ENTRE 18,5 E 25,0|	NORMAL
ENTRE 25,0 E 30,0|	SOBREPESO
ENTRE 30,0 E 40,0|	OBESIDADE
MAIOR QUE 40,0|	OBESIDADE GRAVE

Dica:
\text{IMC} = \frac{\text{peso}}{\text{altura}^2} \text{  , peso em kg, altura em m}

16. Para calcular a raiz quadrada de um número $N>0$ podemos aplicar a seguinte fórmula iterativa:
x_{n+1} = \frac{1}{2}\left(x_n+\frac{N}{x_n}\right)
onde $x_n$ representa a raiz quadrada do número calculada na iteração $n$. As iterações terminam quando $|N - x_n \times x_n| < 10^{-9}$.
Assuma $x_1 = 1$ e implemente a função `raiz(N, show=False)`. Note o parâmetro padrão (default) `show`. Impemente a função de forma que apenas quando `show=True` todos os valores estimados da raiz quadrada sejam impressos. Quando `show=False`, ou for ausente na chamada da função, nada será impresso. Em ambos os casos, o valor estimado da raiz quadrada será retornado pela função.
Exemplos de uso:

>>> print(raiz(5))
2.236067977499978

>>> print(raiz(5, True))
x_1 =  1.00000
x_2 =  3.00000
x_3 =  2.33333
x_4 =  2.23810
x_5 =  2.23607
2.236067977499978

>>> print(raiz(5, False))
2.236067977499978
>>> 
