#(14) Implemente uma função recursiva `div(m, n)` que recebe como argumentos dois números naturais `m` e `n` e devolve o resultado da divisão inteira de `m` por `n`. Não pode recorrer às operações aritméticas de multiplicação, divisão inteira e resto da divisão inteira.

# Define a função div(m, n) para calcular a divisão inteira de m por n
def div(m, n):
    # Verifica se m é menor que n
    if m < n:
        # Se m for menor que n, retorna 0, pois não há divisão inteira possível
        return 0
    else:
        # Se m for maior ou igual a n, calcula a divisão inteira recursivamente
        # Retorna 1 (representando uma vez que o divisor cabe no dividendo)
        # somado ao resultado da função chamada recursivamente com os argumentos m - n e n
        return 1 + div(m - n, n)

# Solicita ao usuário inserir o valor do dividendo m
m = int(input("Digite o valor de m (dividendo): "))

# Solicita ao usuário inserir o valor do divisor n
n = int(input("Digite o valor de n (divisor): "))

# Verifica se o divisor n é zero
if n == 0:
    # Se n for zero, imprime uma mensagem de erro informando que a divisão por zero não é permitida
    print("Erro: divisão por zero!")
else:
    # Se n não for zero, calcula a divisão inteira de m por n chamando a função div(m, n)
    # e imprime o resultado
    print(f"A divisão inteira de {m} por {n} é:", div(m, n))
