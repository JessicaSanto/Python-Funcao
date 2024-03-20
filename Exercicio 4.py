#(4) Implemente uma função que receba um valor em segundos e imprima o correspondente em horas, minutos e segundos. Por exemplo, se a função receber como argumento 4814, imprimirá 1 hora(s) 20 minuto(s) e 14 segundo(s).

def hms(secs):
    # Calcula o número de horas
    h = secs // 3600
    # Calcula o resto dos segundos após a conversão das horas
    rh = secs % 3600
    # Calcula o número de minutos
    m = rh // 60
    # Calcula o número de segundos restantes
    s = rh % 60
    # Imprime o resultado formatado
    print(f"{h} hora(s) {m} minuto(s) {s} segundo(s)")

# Chama a função hms() com diferentes valores de segundos para converter e imprimir o resultado
hms(4814)
hms(3661)
