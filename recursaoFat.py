# FATEC - ESTRUTURAS DE DADOS - PROF. MASANORI
#Recursão para fatorial

def fat(n):
    if n <= 1 : return 1
    return n * fat(n-1)