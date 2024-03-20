#(6) Implemente uma função que retorne a quantidade de dígitos de um determinado número natural passado como argumento. Por exemplo, ao chamar a função com o número 2131, ela deverá retornar 4. Usar apenas operações matemáticas, isto é, não usar operações com strings.

def conta_digito(n):
    # Função para contar quantos dígitos tem o número 'n'
    if n == 0:  # Se 'n' for igual a 0
        return 1  # Retorna 1, pois o número 0 tem apenas 1 dígito
    cont = 0  # Inicializa o contador de dígitos como 0
    rem = n  # Inicializa a variável rem para armazenar o valor de 'n'
    while rem > 0:  # Entra em um loop while enquanto 'rem' for maior que 0
        rem //= 10  # Divide 'rem' por 10 para remover o último dígito
        cont += 1  # Incrementa o contador de dígitos em 1
    return cont  # Retorna o número de dígitos de 'n'

# Testa a função conta_digito() com diferentes valores e imprime os resultados
print(f"0:   {conta_digito(0)}")  # Deve retornar 1
print(f"1:   {conta_digito(1)}")  # Deve retornar 1
print(f"9:   {conta_digito(9)}")  # Deve retornar 1
print(f"10:  {conta_digito(10)}")  # Deve retornar 2
print(f"99:  {conta_digito(99)}")  # Deve retornar 2
print(f"100: {conta_digito(100)}")  # Deve retornar 3
print(f"123: {conta_digito(123)}")  # Deve retornar 3
