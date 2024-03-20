#(2) Implemente uma função que receba um valor `n` inteiro e imprima até a n-ésima linha da seguinte forma:
 #   1
 #   2   2
 #   3   3   3
 #   :   :   :
 #   n   n   n   n   n   n  ... n

def tri(n):
    # Inicializa as variáveis i e j com 0
    i, j = 0, 0
    # Entra em um loop while enquanto i for menor que n
    while i < n:
        # Incrementa i em 1 a cada iteração para controlar o número de elementos em cada linha
        i += 1
        # Reinicia a variável j para 0 a cada nova linha
        j = 0
        # Entra em um loop while enquanto j for menor que i
        while j < i:
            # Imprime o valor de i com um espaço de largura de 3 dígitos
            # Utiliza end=' ' para evitar quebras de linha entre os números na mesma linha
            print(f'{i:3d}', end=' ')
            # Incrementa j em 1 para controlar quantas vezes o valor de i é impresso na mesma linha
            j += 1
        # Imprime uma quebra de linha para passar para a próxima linha
        print()

# Chama a função tri() com o argumento 4 para imprimir um triângulo numérico com 4 linhas
tri(4)
