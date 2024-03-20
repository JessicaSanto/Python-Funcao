#(5) Implemente uma função que retorna `True` se o argumento de entrada for um número natural primo e `False` caso contrário.

def is_prime(n):
    # Função para verificar se um número 'n' é primo
    if n <= 1:  # Verifica se 'n' é menor ou igual a 1
        return False  # Se 'n' for menor ou igual a 1, retorna False, pois números menores que 2 não são primos
    if n == 2:  # Verifica se 'n' é igual a 2
        return True  # Se 'n' for igual a 2, retorna True, pois 2 é um número primo
    i = 2  # Inicia o contador 'i' em 2
    while i <= n/2:  # Entra em um loop while enquanto 'i' for menor ou igual a 'n' dividido por 2
        if n % i == 0:  # Verifica se 'n' é divisível por 'i'
            return False  # Se 'n' for divisível por 'i', retorna False, pois 'n' não é primo
        i += 1  # Incrementa 'i' em 1 para verificar o próximo número
    return True  # Se nenhum divisor for encontrado, retorna True, indicando que 'n' é primo

def eh_primo(numero):
    # Função para verificar se um número 'numero' é primo
    if numero <= 1:  # Verifica se 'numero' é menor ou igual a 1
        return False  # Se 'numero' for menor ou igual a 1, retorna False, pois números menores que 2 não são primos
    for i in range(2, int(numero ** 0.5) + 1):  # Itera de 2 até a raiz quadrada de 'numero' (arredondada para cima)
        if numero % i == 0:  # Verifica se 'numero' é divisível por 'i'
            return False  # Se 'numero' for divisível por 'i', retorna False, pois 'numero' não é primo
    return True  # Se nenhum divisor for encontrado, retorna True, indicando que 'numero' é primo

#
