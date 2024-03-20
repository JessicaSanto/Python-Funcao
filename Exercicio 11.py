#(11) Implemente uma função que recebe um número `n` e retorna a menor potência de 2 maior ou igual a `n`. Por exemplo, `pot2(14)` retornará `16`,  `pot2(42)` retornará `64`. Obs: um algoritmo como esse é usado em processamento de sinais para determinar a ordem da transformada rápida de Fourier.

def pot2a(n):
    # Calcula a próxima potência de 2 que é maior ou igual a 'n' usando um loop while e uma variável de expoente
    exp = 0  # Inicializa o expoente como 0
    while 2 ** exp < n:  # Enquanto 2 elevado à exp for menor que 'n'
        exp += 1  # Incrementa o expoente
    return 2 ** exp  # Retorna 2 elevado à exp

def pot2b(n):
    # Calcula a próxima potência de 2 que é maior ou igual a 'n' usando um loop while e uma variável de potência
    pot = 1  # Inicializa a potência como 1
    while pot < n:  # Enquanto 'pot' for menor que 'n'
        pot *= 2  # Multiplica 'pot' por 2
    return pot  # Retorna 'pot'

# Testa as funções pot2a() e pot2b() para diferentes valores de 'n' e imprime os resultados
for n in [0, 14, 42, 127, 128]:
    print(f"{n:3d} -> {pot2a(n):3d}, {pot2b(n):3d}")  # Imprime o valor de 'n' seguido das potências calculadas por pot2a() e pot2b()
