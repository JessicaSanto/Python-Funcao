#(1) Crie a função python def taboada(n):

#Apresenta a taboada do inteiro n, onde 1 <= n <= 9.
#que reproduz a taboada do número `n` na forma (exemplo para `n` = 7):
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

def taboada(n):
    # Verifica se o número inteiro n está dentro do intervalo válido de 1 a 9
    if 1 <= n <= 9:
        # Se n estiver no intervalo válido, imprime o título da tabuada com o número n
        print(f'\nTaboada do {n}')
        # Imprime uma linha de separação
        print(f'------------')
        # Itera de 0 a 10 (inclusive) para imprimir a tabuada
        for v in range(11):
            # Imprime cada linha da tabuada formatada
            # Utiliza f-strings para formatar a saída
            # {v:2} garante que v seja impresso com pelo menos 2 espaços de largura
            # {n:2} garante que n seja impresso com pelo menos 2 espaços de largura
            # {v*n:2d} garante que o resultado da multiplicação seja impresso como um número inteiro com pelo menos 2 espaços de largura
            print(f'{v:2} x {n:2} = {v*n:2d}')

# Chama a função taboada() com o argumento 7 para imprimir a tabuada do número 7
taboada(7)
