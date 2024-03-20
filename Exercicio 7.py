#(7) Implemente uma função que recebe um numero inteiro e retorne este número escrito ao contrário:
#Entre com um numero inteiro: 12345
#O seu inverso: 54321
#Desenvolva a funcao sem recorrer a operacoes com strings, isto é, utilize apenas operações matemáticas

#Inverte Numero
#Implemente uma função que recebe um numero inteiro e retorne este numero escrito ao contrario:
#Entre com um numero inteiro: 12345
#O seu inverso: 54321
#Desenvolva a funcao sem recorrer a operacoes com strings.
#Utilize apenas operacoes matematicas

def inverte(n):
    # Função para inverter um número inteiro 'n'
    N = n  # Atribui o valor de 'n' a uma variável auxiliar 'N'
    iN = 0  # Inicializa uma variável para armazenar o número invertido
    while N > 0:  # Entra em um loop while enquanto 'N' for maior que 0
        r = N % 10  # Calcula o último dígito de 'N' usando o operador de módulo (%)
        N //= 10  # Remove o último dígito de 'N' dividindo por 10
        iN = iN * 10 + r  # Constrói o número invertido, multiplicando por 10 e adicionando o último dígito
    return iN  # Retorna o número invertido

n = int(input("Entre com um numero inteiro: "))  # Solicita ao usuário para entrar com um número inteiro
print(f'O seu inverso: {inverte(n)}')  # Chama a função 'inverte()' com o número informado e imprime o resultado
