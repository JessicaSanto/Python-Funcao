#(16) Para calcular a raiz quadrada de um número $N>0$ podemos aplicar a seguinte fórmula iterativa:
#x_{n+1} = \frac{1}{2}\left(x_n+\frac{N}{x_n}\right)
#onde $x_n$ representa a raiz quadrada do número calculada na iteração $n$. As iterações terminam quando $|N - x_n \times x_n| < 10^{-9}$.
#Assuma $x_1 = 1$ e implemente a função `raiz(N, show=False)`. Note o parâmetro padrão (default) `show`. Impemente a função de forma que apenas quando `show=True` todos os valores estimados da raiz quadrada sejam impressos. Quando `show=False`, ou for ausente na chamada da função, nada será impresso. Em ambos os casos, o valor estimado da raiz quadrada será retornado pela função.
#Exemplos de uso:
#print(raiz(5))
#2.236067977499978

#print(raiz(5, True))
#x_1 =  1.00000
#x_2 =  3.00000
#x_3 =  2.33333
#x_4 =  2.23810
#x_5 =  2.23607
#2.236067977499978

#print(raiz(5, False))
#2.236067977499978

def raiz(N, show=False):
    # Define um valor muito pequeno para a precisão epsilon
    epsilon = 1e-9
    # Inicializa o valor de x como 1
    x = 1
    # Inicializa o contador de iterações n como 1
    n = 1
    # Entra em um loop enquanto a diferença entre x^2 e N for maior que epsilon
    while abs(x*x - N) > epsilon:
        # Se a opção show for True, imprime o valor atual de x
        if show:
            print(f"x_{n} = {x:8.5f}")
        # Atualiza o valor de x usando o método de Newton-Raphson para encontrar a raiz quadrada de N
        x = 1/2*(x + N/x)
        # Incrementa o contador de iterações
        n += 1
    # Retorna o valor aproximado da raiz quadrada de N
    return x

# Testa a função raiz() com diferentes valores de N e opções show
print(raiz(5, show=True))  # Mostra os valores intermediários durante a iteração
print(raiz(5))  # Calcula a raiz quadrada de 5 sem mostrar os valores intermediários
print(raiz(5, False))  # Calcula a raiz quadrada de 5 sem mostrar os valores intermediários (opção padrão é False)
